import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Data.Nat.Prime.Basic
import ReciprocalTraceCounting

/-!
The rational relative-trace bijection and the exact-order counting transfer.
The source predicates below are actual field powers, orders and expressions.
They do not contain the desired bijection or cardinality as assumptions.
-/

namespace PaperA.RelativeTraceTransfer

abbrev t (s : ℕ) : ℕ := 2 ^ s
abbrev A (s : ℕ) : ℕ := t s + 1
abbrev B (s : ℕ) : ℕ := t s ^ 2 + 1
abbrev d (s : ℕ) : ℕ := A s * B s

def toElement {L : Type*} [Field L] (c γ : L) : L := c / (1 + γ)
def toParameter {L : Type*} [Field L] (c a : L) : L := (a + c) / a
abbrev weight {L : Type*} [Field L] (c γ : L) : L :=
  PaperA.ReciprocalTrace.reciprocalTrace γ c

lemma one_add_ne_zero {L : Type*} [Field L] [CharP L 2]
    {γ : L} (hγ : γ ≠ 1) : 1 + γ ≠ 0 := by
  intro h
  apply hγ
  exact (CharTwo.add_eq_zero.mp h).symm

lemma parameter_element {L : Type*} [Field L] [CharP L 2]
    {c γ : L} (hc : c ≠ 0) (hγ : γ ≠ 1) :
    toParameter c (toElement c γ) = γ := by
  have ha : toElement c γ ≠ 0 := div_ne_zero hc (one_add_ne_zero hγ)
  calc
    toParameter c (toElement c γ) = 1 + c / toElement c γ := by
      simp only [toParameter, add_div, div_self ha]
    _ = 1 + (1 + γ) := by simp [toElement, hc]
    _ = γ := by rw [← add_assoc, CharTwo.add_self_eq_zero, zero_add]

lemma element_parameter {L : Type*} [Field L] [CharP L 2]
    {c a : L} (hc : c ≠ 0) (ha : a ≠ 0) :
    toElement c (toParameter c a) = a := by
  have hden : 1 + (a+c)/a = c/a := by
    calc
      1 + (a+c)/a = (a+(a+c))/a := by simp only [add_div, div_self ha]
      _ = c/a := by rw [← add_assoc, CharTwo.add_self_eq_zero, zero_add]
  simp only [toElement, toParameter, hden]
  simp [hc]

lemma parameter_ne_one {L : Type*} [Field L] [CharP L 2]
    {c a : L} (hc : c ≠ 0) (ha : a ≠ 0) : toParameter c a ≠ 1 := by
  intro h
  have heq : a+c = a := (div_eq_one_iff_eq ha).mp h
  exact hc (add_left_cancel (show a+c = a+0 by simpa using heq))

lemma weight_parameter {L : Type*} [Field L] [CharP L 2]
    {c a : L} (hc : c ≠ 0) (ha : a ≠ 0) (hac : a+c ≠ 0) :
    weight c (toParameter c a) = (a*(a+c))⁻¹ := by
  have hsq : (a+c)^2 = a^2+c^2 := CharTwo.add_sq a c
  unfold weight PaperA.ReciprocalTrace.reciprocalTrace toParameter
  field_simp [ha, hac, hc]
  linear_combination hsq + a^2 * (CharTwo.two_eq_zero (R := L))

lemma element_add {L : Type*} [Field L] [CharP L 2]
    {c γ : L} (hγ : γ ≠ 1) :
    toElement c γ + c = c*γ/(1+γ) := by
  unfold toElement
  apply (eq_div_iff (one_add_ne_zero hγ)).mpr
  rw [add_mul, div_mul_cancel₀ _ (one_add_ne_zero hγ)]
  calc
    c + c*(1+γ) = (c+c)+c*γ := by ring
    _ = c*γ := by rw [CharTwo.add_self_eq_zero, zero_add]

lemma weight_element {L : Type*} [Field L] [CharP L 2]
    {c γ : L} (hc : c ≠ 0) (hγ0 : γ ≠ 0) (hγ1 : γ ≠ 1) :
    (toElement c γ) * (toElement c γ+c) = (weight c γ)⁻¹ := by
  have ha : toElement c γ ≠ 0 := div_ne_zero hc (one_add_ne_zero hγ1)
  have hac : toElement c γ+c ≠ 0 := by
    rw [element_add hγ1]
    exact div_ne_zero (mul_ne_zero hc hγ0) (one_add_ne_zero hγ1)
  have hw := weight_parameter hc ha hac
  rw [parameter_element hc hγ1] at hw
  rw [hw, inv_inv]

lemma t_pos (s : ℕ) : 0 < t s := pow_pos (by decide) s
lemma t_two_le {s : ℕ} (hs : 1 ≤ s) : 2 ≤ t s := by
  cases s with
  | zero => omega
  | succ s =>
    have hp : 0 < 2 ^ s := pow_pos (by decide) s
    change 2 ≤ 2 ^ (s+1)
    rw [pow_succ]
    omega

lemma square_minus_one {t : ℕ} (ht : 1 ≤ t) : t^2-1 = (t+1)*(t-1) := by
  cases t with
  | zero => omega
  | succ k =>
    have h : (k+1)^2 = (k+1+1)*k+1 := by ring
    simp only [h, Nat.add_sub_cancel]

lemma square_plus_one {t : ℕ} (ht : 1 ≤ t) : t^2+1 = 2+(t+1)*(t-1) := by
  cases t with
  | zero => omega
  | succ k => simp only [Nat.add_sub_cancel]; ring

lemma coprime_components {s : ℕ} (hs : 1 ≤ s) : Nat.Coprime (A s) (B s) := by
  have he : Even (t s) := Even.pow_of_ne_zero (by decide : Even 2) (by omega)
  have ho : Odd (t s+1) := he.add_odd (by decide : Odd 1)
  change Nat.Coprime (t s+1) (t s^2+1)
  rw [square_plus_one (by have := t_two_le hs; omega)]
  simpa only [Nat.coprime_add_mul_left_right] using ho.coprime_two_right

lemma coprime_B_t_minus_one {s : ℕ} (hs : 1 ≤ s) :
    Nat.Coprime (B s) (t s-1) := by
  have he : Even (t s) := Even.pow_of_ne_zero (by decide : Even 2) (by omega)
  have hmod : t s % 2 = 0 := Nat.even_iff.mp he
  have ho : Odd (t s-1) := by rw [Nat.odd_iff]; have := t_two_le hs; omega
  change Nat.Coprime (t s^2+1) (t s-1)
  rw [square_plus_one (by have := t_two_le hs; omega)]
  simpa only [Nat.coprime_add_mul_right_left] using ho.coprime_two_left

lemma add_pow_square {L : Type*} [Field L] [CharP L 2]
    (s : ℕ) (x y : L) : (x+y)^(t s^2) = x^(t s^2)+y^(t s^2) := by
  have hp : t s^2 = 2^(2*s) := by simp only [t, ← pow_mul]; congr 1; omega
  rw [hp]
  exact add_pow_char_pow _ _ _ _

lemma root_nonzero {L : Type*} [Field L] {n : ℕ} (hn : 0 < n)
    {z : L} (hz : z^n = 1) : z ≠ 0 := by
  intro h
  have : (0 : L) = 1 := by simpa only [h, zero_pow (Nat.ne_of_gt hn)] using hz
  exact zero_ne_one this

lemma parameter_nonidentity {L : Type*} [Field L] [CharP L 2]
    {s : ℕ} {c γ : L} (hw : weight c γ ^ A s = 1) : γ ≠ 1 := by
  intro h
  have : (0 : L) = 1 := by
    simpa only [h, weight, PaperA.ReciprocalTrace.reciprocalTrace, inv_one,
      CharTwo.add_self_eq_zero, zero_div, zero_pow (Nat.succ_ne_zero _)] using hw
  exact zero_ne_one this

lemma element_frobenius {L : Type*} [Field L] [CharP L 2]
    {s : ℕ} {c γ : L} (hc : c ^ (t s^2) = c)
    (hγ0 : γ ≠ 0) (hγ1 : γ ≠ 1) (hγ : γ ^ B s = 1) :
    toElement c γ ^ (t s^2) = toElement c γ+c := by
  have hgp : γ ^ (t s^2) = γ⁻¹ := PaperA.ReciprocalTrace.pow_eq_inverse hγ
  have hden : (1+γ)^(t s^2) = 1+γ⁻¹ := by
    rw [add_pow_square, one_pow, hgp]
  calc
    toElement c γ ^ (t s^2) = c/(1+γ⁻¹) := by rw [toElement, div_pow, hc, hden]
    _ = c*γ/(1+γ) := by
      field_simp [hγ0]
      ring
    _ = toElement c γ+c := (element_add hγ1).symm

lemma power_minus_one_eq_parameter {L : Type*} [Field L]
    {s : ℕ} {c a : L} (ha : a ≠ 0) (hpow : a^(t s^2) = a+c) :
    a^(t s^2-1) = toParameter c a := by
  apply (eq_div_iff ha).mpr
  have hr : 1 ≤ t s^2 := Nat.one_le_iff_ne_zero.mpr (pow_ne_zero _ (t_pos s).ne')
  rw [← pow_succ, Nat.sub_add_cancel hr, hpow]

lemma element_data {L : Type*} [Field L] [CharP L 2]
    {s : ℕ} {c γ : L} (hc0 : c ≠ 0) (hc : c^(t s^2) = c)
    (hγ : γ^B s = 1) (hw : weight c γ ^ A s = 1) :
    let a := toElement c γ
    a ≠ 0 ∧ a^d s = 1 ∧ a+a^(t s^2) = c ∧
      a^B s = (weight c γ)⁻¹ ∧ a^(t s^2-1) = γ := by
  have hγ0 := root_nonzero (Nat.succ_pos _) hγ
  have hγ1 := parameter_nonidentity hw
  have ha := div_ne_zero hc0 (one_add_ne_zero hγ1)
  have hpow := element_frobenius hc hγ0 hγ1 hγ
  have hnorm : toElement c γ ^ B s = (weight c γ)⁻¹ := by
    change toElement c γ ^ (t s^2+1) = _
    rw [pow_succ, hpow, mul_comm, weight_element hc0 hγ0 hγ1]
  refine ⟨ha, ?_, ?_, hnorm, ?_⟩
  · rw [d, Nat.mul_comm, pow_mul, hnorm, inv_pow, hw, inv_one]
  · rw [hpow]
    exact CharTwo.add_cancel_left _ _
  · rw [power_minus_one_eq_parameter (a := toElement c γ) ha hpow,
      parameter_element hc0 hγ1]

lemma element_nonzero_of_root {L : Type*} [Field L]
    {s : ℕ} {a : L} (ha : a^d s = 1) : a ≠ 0 :=
  root_nonzero (Nat.mul_pos (Nat.succ_pos _) (Nat.succ_pos _)) ha

lemma parameter_data {L : Type*} [Field L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {c a : L} (hc0 : c ≠ 0)
    (haroot : a^d s = 1) (htrace : a+a^(t s^2) = c) :
    let γ := toParameter c a
    γ^B s = 1 ∧ weight c γ ^ A s = 1 ∧
      a^B s = (weight c γ)⁻¹ ∧ a^(t s^2-1) = γ := by
  have ha := element_nonzero_of_root haroot
  have hpow : a^(t s^2) = a+c := by
    simpa only [CharTwo.add_cancel_left] using congrArg (fun z => a+z) htrace
  have hac : a+c ≠ 0 := by rw [← hpow]; exact pow_ne_zero _ ha
  have hparameter := power_minus_one_eq_parameter ha hpow
  have hnorm : a^B s = (weight c (toParameter c a))⁻¹ := by
    rw [weight_parameter hc0 ha hac, inv_inv]
    change a^(t s^2+1) = _
    rw [pow_succ, hpow, mul_comm]
  refine ⟨?_, ?_, hnorm, hparameter⟩
  · rw [← hparameter, ← pow_mul]
    have he : (t s^2-1)*B s = d s*(t s-1) := by
      rw [square_minus_one (by have := t_two_le hs; omega)]
      simp only [d, A]
      ring
    rw [he, pow_mul, haroot, one_pow]
  · have he : (a^B s)^A s = 1 := by
      rw [← pow_mul, Nat.mul_comm, ← d, haroot]
    rw [hnorm, inv_pow, inv_eq_one] at he
    exact he

/-- The full rational bijection, before imposing primitive orders. -/
def traceEquiv {L : Type*} [Field L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {c : L} (hc0 : c ≠ 0) (hc : c^(t s^2) = c) :
    {γ : L // γ^B s = 1 ∧ weight c γ ^ A s = 1} ≃
      {a : L // a^d s = 1 ∧ a+a^(t s^2) = c} where
  toFun γ := ⟨toElement c γ, (element_data hc0 hc γ.2.1 γ.2.2).2.1,
    (element_data hc0 hc γ.2.1 γ.2.2).2.2.1⟩
  invFun a := ⟨toParameter c a, (parameter_data hs hc0 a.2.1 a.2.2).1,
    (parameter_data hs hc0 a.2.1 a.2.2).2.1⟩
  left_inv γ := by
    apply Subtype.ext
    exact parameter_element hc0 (parameter_nonidentity γ.2.2)
  right_inv a := by
    apply Subtype.ext
    exact element_parameter hc0 (element_nonzero_of_root a.2.1)

lemma order_components {L : Type*} [Field L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {a γ w : L} (haroot : a^d s = 1)
    (hB : a^B s = w⁻¹) (hγ : a^(t s^2-1) = γ) :
    orderOf a = d s ↔ orderOf γ = B s ∧ orderOf w = A s := by
  constructor
  · intro ho
    have hpowA : orderOf (a^A s) = B s := by
      have hdvd : A s ∣ orderOf a := by rw [ho]; exact dvd_mul_right _ _
      rw [orderOf_pow_of_dvd (Nat.succ_ne_zero _) hdvd, ho, d,
        Nat.mul_div_cancel_left _ (Nat.succ_pos _)]
    have hpowB : orderOf (a^B s) = A s := by
      have hdvd : B s ∣ orderOf a := by rw [ho]; exact dvd_mul_left _ _
      rw [orderOf_pow_of_dvd (Nat.succ_ne_zero _) hdvd, ho, d,
        Nat.mul_div_cancel _ (Nat.succ_pos _)]
    constructor
    · rw [← hγ, square_minus_one (by have := t_two_le hs; omega), pow_mul]
      have hcop : Nat.Coprime (orderOf (a^A s)) (t s-1) := by
        rw [hpowA]; exact coprime_B_t_minus_one hs
      exact hcop.orderOf_pow.trans hpowA
    · rw [hB, PaperA.ReciprocalTraceCounting.orderOf_inverse_field] at hpowB
      exact hpowB
  · rintro ⟨hgo, hwo⟩
    have hAdvd : A s ∣ orderOf a := by
      have ho : orderOf (a^B s) = A s := by
        rw [hB, PaperA.ReciprocalTraceCounting.orderOf_inverse_field, hwo]
      rw [← ho]
      exact orderOf_pow_dvd _
    have hBdvd : B s ∣ orderOf a := by
      rw [← hgo, ← hγ]
      exact orderOf_pow_dvd _
    exact Nat.dvd_antisymm (orderOf_dvd_of_pow_eq_one haroot)
      ((coprime_components hs).mul_dvd_of_dvd_of_dvd hAdvd hBdvd)

noncomputable def primitiveElements {L : Type*} [Field L] [Fintype L]
    (s : ℕ) (c : L) : Finset L := by
  classical
  exact Finset.univ.filter fun a => a^d s = 1 ∧ orderOf a = d s ∧ a+a^(t s^2) = c

noncomputable def M {L : Type*} [Field L] [Fintype L] (s : ℕ) (c : L) : ℕ :=
  (primitiveElements s c).card

lemma mem_primitiveElements {L : Type*} [Field L] [Fintype L]
    (s : ℕ) (c a : L) : a ∈ primitiveElements s c ↔
      a^d s = 1 ∧ orderOf a = d s ∧ a+a^(t s^2) = c := by
  classical
  simp only [primitiveElements, Finset.mem_filter, Finset.mem_univ, true_and]

lemma primitive_element_of_parameter {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {c γ : L} (hc0 : c ≠ 0) (hc : c^(t s^2) = c)
    (hg : γ ∈ PaperA.ReciprocalTraceCounting.filteredSource
      (t s) c (fun w => orderOf w = A s)) :
    toElement c γ ∈ primitiveElements s c := by
  obtain ⟨hgo, hwroot, hwo⟩ := (PaperA.ReciprocalTraceCounting.mem_filteredSource _ _ _ _).mp hg
  have hgroot : γ^B s = 1 := by
    change γ^(t s^2+1) = 1
    rw [← hgo]
    exact pow_orderOf_eq_one γ
  obtain ⟨_, haroot, htrace, hnorm, hpower⟩ := element_data hc0 hc hgroot hwroot
  exact (mem_primitiveElements _ _ _).mpr
    ⟨haroot, (order_components hs haroot hnorm hpower).mpr ⟨hgo,hwo⟩, htrace⟩

lemma primitive_parameter_of_element {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {c a : L} (hc0 : c ≠ 0)
    (ha : a ∈ primitiveElements s c) :
    toParameter c a ∈ PaperA.ReciprocalTraceCounting.filteredSource
      (t s) c (fun w => orderOf w = A s) := by
  obtain ⟨haroot, hao, htrace⟩ := (mem_primitiveElements _ _ _).mp ha
  obtain ⟨_, hwroot, hnorm, hpower⟩ := parameter_data hs hc0 haroot htrace
  have hh := (order_components hs haroot hnorm hpower).mp hao
  exact (PaperA.ReciprocalTraceCounting.mem_filteredSource _ _ _ _).mpr ⟨hh.1,hwroot,hh.2⟩

theorem M_eq_parameter_count {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {c : L} (hc0 : c ≠ 0) (hc : c^(t s^2) = c) :
    M s c = (PaperA.ReciprocalTraceCounting.filteredSource
      (t s) c (fun w => orderOf w = A s)).card := by
  classical
  unfold M
  symm
  apply Finset.card_bij (fun γ _ => toElement c γ)
  · intro γ hγ
    exact primitive_element_of_parameter hs hc0 hc hγ
  · intro γ hγ δ hδ heq
    have hg := (PaperA.ReciprocalTraceCounting.mem_filteredSource _ _ _ _).mp hγ
    have hd := (PaperA.ReciprocalTraceCounting.mem_filteredSource _ _ _ _).mp hδ
    have h := congrArg (toParameter c) heq
    rwa [parameter_element hc0 (parameter_nonidentity hg.2.1),
      parameter_element hc0 (parameter_nonidentity hd.2.1)] at h
  · intro a ha
    have hroot := ((mem_primitiveElements _ _ _).mp ha).1
    exact ⟨toParameter c a, primitive_parameter_of_element hs hc0 ha,
      element_parameter hc0 (element_nonzero_of_root hroot)⟩

theorem M_eq_two_mul_support_count {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {c : L} (hc0 : c ≠ 0) (hc : c^(t s^2) = c) :
    M s c = 2 * (PaperA.ReciprocalTraceCounting.filteredSupport
      (t s) c (fun w => orderOf w = A s)).card := by
  rw [M_eq_parameter_count hs hc0 hc]
  exact PaperA.ReciprocalTraceCounting.filtered_source_card_eq_two_mul_support_card
    (t_two_le hs) hc0 _

lemma weight_shift {L : Type*} [Field L] (h u γ : L) :
    weight (h*u) γ = weight h γ * (u⁻¹)^2 := by
  simp only [weight, PaperA.ReciprocalTrace.reciprocalTrace, mul_pow,
    div_eq_mul_inv, mul_inv, inv_pow]
  ring

lemma shifted_power_one {L : Type*} [Field L] {s : ℕ} {u : L}
    (hu : u^A s = 1) : ((u⁻¹)^2)^A s = 1 := by
  rw [← pow_mul, Nat.mul_comm, pow_mul, inv_pow, hu, inv_one, one_pow]

lemma shifted_source_eq {L : Type*} [Field L] [Fintype L]
    {s : ℕ} (h u : L) (hu : u^A s = 1) :
    PaperA.ReciprocalTraceCounting.filteredSource (t s) (h*u) (fun z => orderOf z = A s) =
      PaperA.ReciprocalTraceCounting.filteredSource (t s) h
        (fun z => orderOf (z*(u⁻¹)^2) = A s) := by
  classical
  ext γ
  simp only [PaperA.ReciprocalTraceCounting.mem_filteredSource]
  change (orderOf γ = B s ∧ weight (h*u) γ ^ A s = 1 ∧ orderOf (weight (h*u) γ) = A s) ↔ _
  rw [weight_shift, mul_pow, shifted_power_one hu, mul_one]

lemma fixed_shift {L : Type*} [Field L] {s : ℕ} {h u : L}
    (hh : h^t s = h) (hu : u^A s = 1) : (h*u)^(t s^2) = h*u := by
  rw [mul_pow, pow_two, pow_mul, hh, hh]
  rw [← pow_two]
  exact congrArg (fun z => h*z) (PaperA.ReciprocalTrace.norm_one_quadratic_fixed hu)

theorem M_shifted_support_count {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) {h u : L} (hh0 : h ≠ 0)
    (hh : h^t s = h) (hu : u^A s = 1) :
    M s (h*u) = 2 * (PaperA.ReciprocalTraceCounting.filteredSupport
      (t s) h (fun z => orderOf (z*(u⁻¹)^2) = A s)).card := by
  have hu0 : u ≠ 0 := root_nonzero (Nat.succ_pos _) hu
  rw [M_eq_parameter_count hs (mul_ne_zero hh0 hu0) (fixed_shift hh hu),
    shifted_source_eq h u hu]
  exact PaperA.ReciprocalTraceCounting.filtered_source_card_eq_two_mul_support_card
    (t_two_le hs) hh0 _

theorem finite_base_M_shifted_support_count (K L : Type*)
    [Field K] [Fintype K] [Field L] [Fintype L] [Algebra K L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) (hcard : Fintype.card K = t s)
    (h : K) (hh : h ≠ 0) (u : L) (hu : u^A s = 1) :
    M s (algebraMap K L h * u) =
      2 * (PaperA.ReciprocalTraceCounting.filteredSupport
        (t s) (algebraMap K L h) (fun z => orderOf (z*(u⁻¹)^2) = A s)).card := by
  apply M_shifted_support_count hs ((map_ne_zero (algebraMap K L)).mpr hh) _ hu
  rw [← hcard]
  exact (FiniteField.frobeniusAlgHom K L).commutes h

theorem M_zero {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) : M (L := L) s 0 = 0 := by
  classical
  unfold M
  rw [Finset.card_eq_zero]
  apply Finset.eq_empty_iff_forall_notMem.mpr
  intro a ha
  obtain ⟨haroot, hao, hatrace⟩ := (mem_primitiveElements _ _ _).mp ha
  have ha0 := element_nonzero_of_root haroot
  have hpow : a^(t s^2) = a+0 := by
    simpa only [CharTwo.add_cancel_left] using congrArg (fun z => a+z) hatrace
  have hpower : a^(t s^2-1) = 1 := by
    rw [power_minus_one_eq_parameter ha0 hpow, toParameter, add_zero, div_self ha0]
  have hdiv : d s ∣ t s^2-1 := by
    rw [← hao]
    exact orderOf_dvd_of_pow_eq_one hpower
  have hr : 4 ≤ t s^2 := by
    simpa only [pow_two] using Nat.mul_le_mul (t_two_le hs) (t_two_le hs)
  have he : d s = B s + t s*B s := by simp only [d, A]; ring
  have hdle : d s ≤ t s^2-1 := Nat.le_of_dvd (by omega) hdiv
  change (t s+1)*(t s^2+1) = (t s^2+1)+t s*(t s^2+1) at he
  change (t s+1)*(t s^2+1) ≤ t s^2-1 at hdle
  omega

end PaperA.RelativeTraceTransfer
