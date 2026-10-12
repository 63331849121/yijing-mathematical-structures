import Mathlib

/-!
# M1：仿射 Singer 层生成 AGL(1, K)（Paper A §5 / 语料 D17 主猜想）
-/

namespace AGL

variable {K : Type*} [Field K]

lemma add_self (h2 : (2 : K) = 0) (x : K) : x + x = 0 := by
  calc
    x + x = (1 + 1) * x := by ring
    _ = (2 : K) * x := by norm_num
    _ = 0 * x := by rw [h2]
    _ = 0 := by ring

lemma neg_self (h2 : (2 : K) = 0) (x : K) : -x = x := by
  calc
    -x = -x + 0 := by rw [add_zero]
    _ = -x + (x + x) := by rw [add_self h2 x]
    _ = x := by ring

def tau (b : K) : K → K := fun x => x + b

def Tf (a c : K) : K → K := fun x => a * x + c

def Tinv (a c : K) : K → K := fun x => a⁻¹ * (x - c)

lemma Tinv_Tf (a : K) (ha : a ≠ 0) (c x : K) : Tinv a c (Tf a c x) = x := by
  unfold Tinv Tf
  field_simp [ha]
  ring

lemma Tf_Tinv (a : K) (ha : a ≠ 0) (c x : K) : Tf a c (Tinv a c x) = x := by
  unfold Tinv Tf
  field_simp [ha]
  ring

def Sf (a c : K) : K → K := fun x => (1 + a) * x + c

def Df (a c : K) : K → K := fun x => (1 + a)⁻¹ * (x - c)

lemma Df_Sf (a : K) (h1 : 1 + a ≠ 0) (c x : K) : Df a c (Sf a c x) = x := by
  unfold Df Sf
  field_simp [h1]
  ring

lemma Sf_Df (a : K) (h1 : 1 + a ≠ 0) (c x : K) : Sf a c (Df a c x) = x := by
  unfold Df Sf
  field_simp [h1]
  ring

lemma slope_id (a : K) (h2 : (2 : K) = 0) (h1 : 1 + a ≠ 0) :
    a * (1 + a)⁻¹ + 1 = (1 + a)⁻¹ := by
  field_simp [h1]
  calc
    a + (1 + a) = 1 + (a + a) := by ring
    _ = 1 + 0 := by rw [add_self h2 a]
    _ = 1 := by ring

theorem not_commute (a c : K) (h2 : (2 : K) = 0) (h1 : 1 + a ≠ 0) (hc : c ≠ 0) :
    Tf a c ∘ Df a c ≠ Df a c ∘ Tf a c := by
  intro h
  have hv := congrFun h 0
  unfold Function.comp Tf Df at hv
  simp only [mul_zero, zero_add] at hv
  have hR : (1 + a)⁻¹ * (c - c) = 0 := by
    rw [sub_self, mul_zero]
  rw [hR] at hv
  have hneg : 0 - c = c := by
    rw [zero_sub, neg_self h2 c]
  rw [hneg] at hv
  have hval : a * ((1 + a)⁻¹ * c) + c = (1 + a)⁻¹ * c := by
    calc
      a * ((1 + a)⁻¹ * c) + c = (a * (1 + a)⁻¹ + 1) * c := by ring
      _ = (1 + a)⁻¹ * c := by rw [slope_id a h2 h1]
  rw [hval] at hv
  have hγc : (1 + a)⁻¹ * c ≠ 0 := mul_ne_zero (inv_ne_zero h1) hc
  exact hγc hv

theorem conj_tau (a b c : K) (_h2 : (2 : K) = 0) (ha : a ≠ 0) (x : K) :
    Tf a c (tau b (Tinv a c x)) = tau (a * b) x := by
  unfold Tf Tinv tau
  field_simp [ha]
  ring

theorem comm_is_translation (a c : K) (_h2 : (2 : K) = 0) (h1 : 1 + a ≠ 0)
    (ha : a ≠ 0) (x : K) : Tf a c (Df a c (Tinv a c (Sf a c x))) = x + (c / (1 + a)) := by
  unfold Tf Df Tinv Sf
  field_simp [h1, ha]
  ring_nf

/-! ## M1.2：仿射群 AGL(1,K)（双字段结构） -/

structure Aff (K : Type*) [Field K] where
  u : Kˣ
  v : K

namespace Aff

variable {K : Type*} [Field K]

def one : Aff K := { u := 1, v := 0 }
def mul (g h : Aff K) : Aff K := { u := g.u * h.u, v := (g.u : K) * h.v + g.v }
def inv (g : Aff K) : Aff K := { u := g.u⁻¹, v := -((g.u⁻¹ : K) * g.v) }

instance : One (Aff K) := { one := one }
instance : Mul (Aff K) := ⟨mul⟩
instance : Inv (Aff K) := ⟨inv⟩
instance : Div (Aff K) := ⟨fun g h => g * h⁻¹⟩

theorem ext (g h : Aff K) (hu : g.u = h.u) (hv : g.v = h.v) : g = h := by
  cases g with
  | mk gu gv =>
    cases h with
    | mk hu' hv' =>
      have hu'eq : gu = hu' := by simpa using hu
      have hv'eq : gv = hv' := by simpa using hv
      rw [hu'eq, hv'eq]

@[simp] lemma one_u : (1 : Aff K).u = 1 := rfl
@[simp] lemma one_v : (1 : Aff K).v = 0 := rfl
@[simp] lemma mul_u (g h : Aff K) : (g * h).u = g.u * h.u := rfl
@[simp] lemma mul_v (g h : Aff K) : (g * h).v = (g.u : K) * h.v + g.v := rfl
@[simp] lemma inv_u (g : Aff K) : (g⁻¹).u = g.u⁻¹ := rfl
@[simp] lemma inv_v (g : Aff K) : (g⁻¹).v = -((g.u⁻¹ : K) * g.v) := rfl
@[simp] lemma units_val_mul (u v : Kˣ) : (u * v).val = u.val * v.val := rfl
@[simp] lemma units_val_one : (1 : Kˣ).val = 1 := rfl
@[simp] lemma units_coe_val (u : Kˣ) : (u : K) = u.val := rfl
lemma units_val_inv (u : Kˣ) : (u⁻¹).val = (u.val)⁻¹ := by
  have h : u.val * (u⁻¹).val = 1 := by
    simpa [units_val_mul, units_val_one] using congrArg Units.val (mul_inv_cancel u)
  exact eq_inv_of_mul_eq_one_right h

lemma units_coe_inv (u : Kˣ) : ((u : K))⁻¹ = ((u⁻¹ : Kˣ) : K) := by
  rw [units_coe_val, units_coe_val, units_val_inv]
@[simp] lemma u_mk (a : Kˣ) (b : K) : ({ u := a, v := b } : Aff K).u = a := rfl
@[simp] lemma v_mk (a : Kˣ) (b : K) : ({ u := a, v := b } : Aff K).v = b := rfl

instance : Group (Aff K) where
  mul_assoc := by
    intro a b c
    apply ext
    · simp [mul_u, mul_assoc]
    · simp [mul_v, mul_u, units_val_mul]; try ring
  one_mul := by
    intro a
    apply ext
    · simp [mul_u, one_u, one_mul]
    · simp [mul_v, mul_u, one_u, one_v, units_val_mul, units_val_one]; try ring
  mul_one := by
    intro a
    apply ext
    · simp [mul_u, one_u, mul_one]
    · simp [mul_v, mul_u, one_v, units_val_mul]; try ring
  inv_mul_cancel := by
    intro a
    apply ext
    · simp [mul_u, inv_u]
    · simp [mul_v, inv_v, mul_u, inv_u, units_val_mul]
  div_eq_mul_inv := by intro a b; rfl

/-- 平移 τ_v = (1, v) -/
def tr (v : K) : Aff K := { u := 1, v := v }
@[simp] lemma tr_u (v : K) : (tr v).u = 1 := rfl
@[simp] lemma tr_v (v : K) : (tr v).v = v := rfl

/-- 非零元 → 单位 -/
def unitOf (a : K) (ha : a ≠ 0) : Kˣ :=
  { val := a, inv := a⁻¹, val_inv := mul_inv_cancel₀ ha, inv_val := inv_mul_cancel₀ ha }

@[simp] lemma unitOf_val (a : K) (ha : a ≠ 0) : (unitOf a ha).val = a := rfl
@[simp] lemma unitOf_inv_val (a : K) (ha : a ≠ 0) : ((unitOf a ha)⁻¹).val = a⁻¹ := rfl

/-- T = (a, c) -/
def Tel (a : K) (ha : a ≠ 0) (c : K) : Aff K := { u := unitOf a ha, v := c }

/-- S = (1+a, c) = id + T；D := S⁻¹ -/
def Sel (a : K) (h1 : 1 + a ≠ 0) (c : K) : Aff K := { u := unitOf (1 + a) h1, v := c }

@[simp] lemma Tel_inv (a : K) (ha : a ≠ 0) (c : K) :
    (Tel a ha c)⁻¹ = { u := (unitOf a ha)⁻¹, v := -(((unitOf a ha)⁻¹ : K) * c) } := rfl

@[simp] lemma Sel_inv (a : K) (h1 : 1 + a ≠ 0) (c : K) :
    (Sel a h1 c)⁻¹ = { u := (unitOf (1 + a) h1)⁻¹, v := -(((unitOf (1 + a) h1)⁻¹ : K) * c) } := rfl

/-- 作用 act g x = u·x + v -/
def act (g : Aff K) (x : K) : K := (g.u : K) * x + g.v

@[simp] lemma act_one (x : K) : act 1 x = x := by
  unfold act
  rw [one_u, one_v, units_coe_val, units_val_one]
  ring

@[simp] lemma act_tr (v x : K) : act (tr v) x = x + v := by
  unfold act tr
  rw [units_coe_val, units_val_one]
  ring

@[simp] lemma act_mul (g h : Aff K) (x : K) : act (g * h) x = act g (act h x) := by
  unfold act
  rw [mul_u, mul_v, units_val_mul, units_coe_val]
  ring

@[simp] lemma act_Tel (a : K) (ha : a ≠ 0) (c x : K) : act (Tel a ha c) x = Tf a c x := by
  simp [act, Tel, Tf]

@[simp] lemma act_Sel (a : K) (h1 : 1 + a ≠ 0) (c x : K) : act (Sel a h1 c) x = Sf a c x := by
  simp [act, Sel, Sf]

@[simp] lemma act_Tinv_el (a : K) (ha : a ≠ 0) (c x : K) : act ((Tel a ha c)⁻¹) x = Tinv a c x := by
  rw [Tel_inv]
  unfold act
  rw [u_mk, v_mk]
  rw [units_coe_inv, units_coe_val, unitOf_inv_val]
  unfold Tinv
  ring

@[simp] lemma act_Dinv_el (a : K) (h1 : 1 + a ≠ 0) (c x : K) : act ((Sel a h1 c)⁻¹) x = Df a c x := by
  rw [Sel_inv]
  unfold act
  rw [u_mk, v_mk]
  rw [units_coe_inv, units_coe_val, unitOf_inv_val]
  unfold Df
  ring

/-- 作用在 0 与 1 两点相同 ⟹ 元素相等 -/
theorem ext_act (g h : Aff K) (h0 : act g 0 = act h 0) (h1p : act g 1 = act h 1) : g = h := by
  apply ext
  · apply Units.ext
    have hv : g.v = h.v := by simpa [act] using h0
    have hu1 : (g.u : K) * 1 + g.v = (h.u : K) * 1 + h.v := by simpa [act] using h1p
    calc
      (g.u : K) = (g.u : K) * 1 + g.v - g.v := by ring
      _ = (h.u : K) * 1 + h.v - g.v := by rw [hu1]
      _ = (h.u : K) := by rw [hv]; ring
  · simpa [act] using h0

/-- 换位子 [T,D] = T·D·T⁻¹·D⁻¹（D = S⁻¹） -/
def Comm (a : K) (ha : a ≠ 0) (h1 : 1 + a ≠ 0) (c : K) : Aff K :=
  Tel a ha c * (Sel a h1 c)⁻¹ * (Tel a ha c)⁻¹ * Sel a h1 c

/-- 换位子的作用 = x + c/(1+a) -/
theorem comm_action (a c : K) (h2 : (2 : K) = 0) (ha : a ≠ 0) (h1 : 1 + a ≠ 0)
    (x : K) : act (Comm a ha h1 c) x = x + (c / (1 + a)) := by
  calc
    act (Tel a ha c * (Sel a h1 c)⁻¹ * (Tel a ha c)⁻¹ * Sel a h1 c) x
        = act (Tel a ha c) (act ((Sel a h1 c)⁻¹) (act ((Tel a ha c)⁻¹) (act (Sel a h1 c) x))) := by
            simp [act_mul]
    _ = Tf a c (Df a c (Tinv a c (Sf a c x))) := by
            simp only [act_Tel, act_Sel, act_Tinv_el, act_Dinv_el]
    _ = x + (c / (1 + a)) := by
            exact comm_is_translation a c h2 h1 ha x

/-- [T,D] = 平移 c/(1+a)（元素等式） -/
theorem comm_eq_tr (a c : K) (h2 : (2 : K) = 0) (ha : a ≠ 0) (h1 : 1 + a ≠ 0) :
    Comm a ha h1 c = tr (c / (1 + a)) := by
  apply ext_act
  · calc
      act (Comm a ha h1 c) 0 = 0 + c / (1 + a) := comm_action a c h2 ha h1 0
      _ = act (tr (c / (1 + a))) 0 := by simp [act_tr]
  · calc
      act (Comm a ha h1 c) 1 = 1 + c / (1 + a) := comm_action a c h2 ha h1 1
      _ = act (tr (c / (1 + a))) 1 := by simp [act_tr]

/-! ## M1.3：closure {T,D} = ⊤ -/

/-- T·τ_b·T⁻¹ = τ_{a·b}（Aff 级共轭平移） -/
lemma conj_tr (a b c : K) (ha : a ≠ 0) (h2 : (2 : K) = 0) :
    Tel a ha c * tr b * (Tel a ha c)⁻¹ = tr (a * b) := by
  apply ext_act
  · calc
      act (Tel a ha c * tr b * (Tel a ha c)⁻¹) 0
          = Tf a c (tau b (Tinv a c 0)) := by
              simp only [act_mul, act_Tel, act_tr, act_Tinv_el, tau]
      _ = 0 + a * b := by
              simpa [tau] using conj_tau a b c h2 ha 0
      _ = act (tr (a * b)) 0 := by
              simp [act_tr]
  · calc
      act (Tel a ha c * tr b * (Tel a ha c)⁻¹) 1
          = Tf a c (tau b (Tinv a c 1)) := by
              simp only [act_mul, act_Tel, act_tr, act_Tinv_el, tau]
      _ = 1 + a * b := by
              simpa [tau] using conj_tau a b c h2 ha 1
      _ = act (tr (a * b)) 1 := by
              simp [act_tr]

/-- 剥离平移得纯乘子：(a,c)·τ_{c/a} = (a,0)（特征 2） -/
lemma mul_extract (a c : K) (ha : a ≠ 0) (h2 : (2 : K) = 0) :
    Tel a ha c * tr (c / a) = { u := unitOf a ha, v := 0 } := by
  apply ext
  · simp [mul_u, tr_u, Tel]
  · simp [mul_v, tr_v, units_coe_val, unitOf_val, Tel]
    field_simp [ha]
    rw [show c * (1 + 1) = c + c from by ring]
    exact add_self h2 c

lemma unitOf_pow (a : K) (ha : a ≠ 0) (n : ℕ) :
    (unitOf a ha) ^ n = unitOf (a ^ n) (pow_ne_zero n ha) := by
  apply Units.ext
  induction n with
  | zero => simp [unitOf_val]
  | succ n ih => simp [pow_succ, units_val_mul, unitOf_val, ih]

lemma unitOf_eq (u0 : Kˣ) (hu0 : u0.val ≠ 0) : unitOf (u0.val) hu0 = u0 := by
  apply Units.ext
  simp [unitOf_val]
lemma mul0_pow_u (u0 : Kˣ) (n : ℕ) : (({ u := u0, v := 0 } : Aff K) ^ n).u = u0 ^ n := by
  induction n with
  | zero => simp
  | succ n ih => simp [pow_succ, mul_u, ih]

lemma mul0_pow_v (u0 : Kˣ) (n : ℕ) : (({ u := u0, v := 0 } : Aff K) ^ n).v = 0 := by
  induction n with
  | zero => simp
  | succ n ih => simp [pow_succ, mul_v, mul0_pow_u, ih]

/-- 终局：本原 a 生成 K* 时，⟨T,D⟩ = 全体仿射群 AGL(1,K) -/
theorem closure_eq_top (a c : K) (ha : a ≠ 0) (h1 : 1 + a ≠ 0) (hc : c ≠ 0) (h2 : (2 : K) = 0)
    (hprim : ∀ w : K, w ≠ 0 → ∃ n : ℕ, w = a ^ n) :
    Subgroup.closure ({Tel a ha c, (Sel a h1 c)⁻¹} : Set (Aff K)) = ⊤ := by
  let H : Subgroup (Aff K) := Subgroup.closure ({Tel a ha c, (Sel a h1 c)⁻¹} : Set (Aff K))
  apply le_antisymm
  · exact le_top
  · intro g hg
    rcases g with ⟨u0, v0⟩
    have hT : Tel a ha c ∈ H := Subgroup.subset_closure (by simp)
    have hD : (Sel a h1 c)⁻¹ ∈ H := Subgroup.subset_closure (by simp)
    have hDinv : Sel a h1 c ∈ H := by simpa only [inv_inv] using H.inv_mem hD
    have hComm : Comm a ha h1 c ∈ H := by
      change Tel a ha c * (Sel a h1 c)⁻¹ * (Tel a ha c)⁻¹ * Sel a h1 c ∈ H
      exact H.mul_mem (H.mul_mem (H.mul_mem hT hD) (H.inv_mem hT)) hDinv
    let δ : K := c / (1 + a)
    have hδ : tr δ ∈ H := by
      simpa [δ, comm_eq_tr a c h2 ha h1] using hComm
    have hconj : ∀ b : K, tr b ∈ H → tr (a * b) ∈ H := by
      intro b hb
      have hmid : Tel a ha c * tr b * (Tel a ha c)⁻¹ ∈ H :=
        H.mul_mem (H.mul_mem hT hb) (H.inv_mem hT)
      rw [conj_tr a b c ha h2] at hmid
      exact hmid
    have hpow : ∀ n : ℕ, tr (a ^ n * δ) ∈ H := by
      intro n
      induction n with
      | zero =>
          simpa using hδ
      | succ n ih =>
          rw [pow_succ', mul_assoc]
          exact hconj (a ^ n * δ) ih
    have hδne : δ ≠ 0 := div_ne_zero hc h1
    have htr_all : ∀ v : K, tr v ∈ H := by
      intro v
      by_cases hv : v = 0
      · rw [hv]
        have : tr (0 : K) = 1 := by apply ext <;> simp [tr]
        rw [this]
        exact H.one_mem
      · have hvδ : v * δ⁻¹ ≠ 0 := mul_ne_zero hv (inv_ne_zero hδne)
        rcases hprim (v * δ⁻¹) hvδ with ⟨n, hn⟩
        have hv' : v = a ^ n * δ := by
          calc
            v = (v * δ⁻¹) * δ := by field_simp [hδne]
            _ = a ^ n * δ := by rw [hn]
        rw [hv']
        exact hpow n
    have hmult0 : ({ u := unitOf a ha, v := 0 } : Aff K) ∈ H := by
      have hm : Tel a ha c * tr (c / a) ∈ H := H.mul_mem hT (htr_all (c / a))
      simpa [mul_extract a c ha h2] using hm
    have hu0ne : u0.val ≠ 0 := by
      intro h
      have hv := u0.val_inv
      rw [h, zero_mul] at hv
      exact one_ne_zero hv.symm
    have hpow_mul : ∀ n : ℕ, ({ u := unitOf a ha, v := 0 } : Aff K) ^ n ∈ H := by
      intro n
      induction n with
      | zero => simpa using H.one_mem
      | succ n ih => simpa [pow_succ] using H.mul_mem ih hmult0
    have hmult : ({ u := u0, v := 0 } : Aff K) ∈ H := by
      rcases hprim u0.val hu0ne with ⟨n, hn⟩
      have hconv : ({ u := unitOf a ha, v := 0 } : Aff K) ^ n = ({ u := u0, v := 0 } : Aff K) := by
        apply ext
        · rw [mul0_pow_u]
          calc
            (unitOf a ha) ^ n = unitOf (a ^ n) (pow_ne_zero n ha) := unitOf_pow a ha n
            _ = unitOf (u0.val) hu0ne := by
              apply Units.ext
              simpa [unitOf_val] using hn.symm
            _ = u0 := unitOf_eq u0 hu0ne
        · rw [mul0_pow_v]
      simpa [hconv] using hpow_mul n
    have htr_v0 : tr (v0 / u0.val) ∈ H := htr_all (v0 / u0.val)
    have hprod : ({ u := u0, v := 0 } : Aff K) * tr (v0 / u0.val) ∈ H := H.mul_mem hmult htr_v0
    have hg : ({ u := u0, v := 0 } : Aff K) * tr (v0 / u0.val) = { u := u0, v := v0 } := by
      apply ext
      · simp [mul_u, tr_u]
      · simp [mul_v, tr_v, units_coe_val]
        field_simp [hu0ne]
    rw [hg] at hprod
    exact hprod

end Aff

end AGL















