import Mathlib.Algebra.Field.ZMod
import InverseSupportGrid

/-!+# A genuine cyclic exponent interface for the inverse-support argument

This module proves that being a unit in `ZMod n` is equivalent to full
additive order `n`. It then proves unit detection under a quotient `m ∣ n`
which retains every prime divisor, and uses actual CRT for `m = p*q`.
No unit-detection conclusion is taken as a hypothesis.

The last covering theorems apply to non-squarefree `n`, including prime-power
lifts of `p*q`. They do not formalize finite-field Frobenius, the certificate
arithmetic, or the fibre/kernel cardinality `n/(p*q)`.
-/

namespace PaperA.CyclicSupport

open PaperA.InverseSupportGrid

theorem coprime_prime_support_reduction {n m : ℕ} (hm : m ∣ n)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ m) (a : ℕ) :
    a.Coprime n ↔ a.Coprime m := by
  constructor
  · intro ha
    exact ha.coprime_dvd_right hm
  · intro ha
    apply Classical.byContradiction
    intro hn
    obtain ⟨r, hr, hra, hrn⟩ := Nat.Prime.not_coprime_iff_dvd.mp hn
    exact (Nat.Prime.not_coprime_iff_dvd.mpr ⟨r, hr, hra, hpr r hr hrn⟩) ha

def quotient {n m : ℕ} (hm : m ∣ n) : ZMod n →+* ZMod m :=
  ZMod.castHom hm (ZMod m)

theorem isUnit_quotient_iff {n m : ℕ} [NeZero n] (hm : m ∣ n)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ m) (z : ZMod n) :
    IsUnit z ↔ IsUnit (quotient hm z) := by
  obtain ⟨a, rfl⟩ := ZMod.natCast_zmod_surjective z
  simpa only [map_natCast, ZMod.isUnit_iff_coprime] using
    coprime_prime_support_reduction hm hpr a

theorem isUnit_iff_full_addOrder {n : ℕ} [NeZero n] (z : ZMod n) :
    IsUnit z ↔ addOrderOf z = n := by
  obtain ⟨a, rfl⟩ := ZMod.natCast_zmod_surjective z
  rw [ZMod.isUnit_iff_coprime, ZMod.addOrderOf_coe a (NeZero.ne n)]
  constructor
  · intro h
    rw [h.symm.gcd_eq_one, Nat.div_one]
  · intro h
    rcases Nat.div_eq_self.mp h with hn | hg
    · exact False.elim ((NeZero.ne n) hn)
    · exact (Nat.coprime_iff_gcd_eq_one.mpr hg).symm

theorem prime_support_prime_powers (p q a b : ℕ) :
    ∀ r : ℕ, r.Prime → r ∣ p ^ (a+1) * q ^ (b+1) → r ∣ p*q := by
  intro r hr hd
  rcases hr.dvd_mul.mp hd with hp | hq
  · exact dvd_mul_of_dvd_left (hr.dvd_of_dvd_pow hp) q
  · exact dvd_mul_of_dvd_right (hr.dvd_of_dvd_pow hq) p

theorem product_dvd_prime_powers (p q a b : ℕ) :
    p*q ∣ p ^ (a+1) * q ^ (b+1) := by
  refine ⟨p^a*q^b, ?_⟩
  rw [pow_succ, pow_succ]
  ac_rfl

theorem isUnit_mod513_iff_mod57 (z : ZMod 513) :
    IsUnit z ↔ IsUnit (quotient (by decide : 57 ∣ 513) z) := by
  apply isUnit_quotient_iff
  exact prime_support_prime_powers 3 19 2 0

noncomputable def coordinates {n p q : ℕ} (hm : p*q ∣ n)
    (hc : p.Coprime q) : ZMod n →+* ZMod p × ZMod q :=
  (ZMod.chineseRemainder hc).toRingHom.comp (quotient hm)

theorem isUnit_iff_coordinates {n p q : ℕ} [NeZero n]
    [Fact p.Prime] [Fact q.Prime] (hm : p*q ∣ n) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ p*q) (z : ZMod n) :
    IsUnit z ↔ (coordinates hm hc z).1 ≠ 0 ∧ (coordinates hm hc z).2 ≠ 0 := by
  rw [isUnit_quotient_iff hm hpr]
  rw [← MulEquiv.isUnit_map (ZMod.chineseRemainder hc)]
  change IsUnit (coordinates hm hc z) ↔ _
  rw [Prod.isUnit_iff, isUnit_iff_ne_zero, isUnit_iff_ne_zero]

theorem isUnit_sub_two_iff_coordinates {n p q : ℕ} [NeZero n]
    [Fact p.Prime] [Fact q.Prime] (hm : p*q ∣ n) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ p*q) (z u : ZMod n) :
    IsUnit (z-2*u) ↔
      (coordinates hm hc z).1 ≠ 2*(coordinates hm hc u).1 ∧
      (coordinates hm hc z).2 ≠ 2*(coordinates hm hc u).2 := by
  rw [isUnit_iff_coordinates hm hc hpr]
  simp only [map_sub, map_mul, map_ofNat, Prod.fst_sub, Prod.snd_sub,
    Prod.fst_mul, Prod.snd_mul, Prod.fst_ofNat, Prod.snd_ofNat, sub_ne_zero]

def imageSupport {n : ℕ} {A B : Type} (π : ZMod n → A × B)
    (S : ZMod n → Prop) (x : A × B) : Prop :=
  ∃ z, S z ∧ π z = x

theorem no_unit_iff_cover {n p q : ℕ} [NeZero n]
    [Fact p.Prime] [Fact q.Prime] (hm : p*q ∣ n) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ p*q)
    (S : ZMod n → Prop) (u : ZMod n) :
    (¬ ∃ z, S z ∧ IsUnit (z-2*u)) ↔
      Cover (imageSupport (coordinates hm hc) S)
        (2*(coordinates hm hc u).1, 2*(coordinates hm hc u).2) := by
  classical
  constructor
  · intro hn x hx
    obtain ⟨z, hz, rfl⟩ := hx
    have hbad : ¬ IsUnit (z-2*u) := fun hu => hn ⟨z,hz,hu⟩
    have hbad' := mt (isUnit_sub_two_iff_coordinates hm hc hpr z u).mpr hbad
    by_cases h1 : (coordinates hm hc z).1 = 2*(coordinates hm hc u).1
    · exact Or.inl h1
    · apply Or.inr
      apply Classical.byContradiction
      intro h2
      exact hbad' ⟨h1,h2⟩
  · intro hcov hgood
    obtain ⟨z,hz,hunit⟩ := hgood
    have hcoords := (isUnit_sub_two_iff_coordinates hm hc hpr z u).mp hunit
    have hbad := hcov (coordinates hm hc z) ⟨z,hz,rfl⟩
    cases hbad with
    | inl h => exact hcoords.1 h
    | inr h => exact hcoords.2 h

theorem nonzero_ne_neg_prime {p : ℕ} [hp : Fact p.Prime] (hodd : p ≠ 2)
    {a : ZMod p} (ha : a ≠ 0) : a ≠ -a := by
  have hcop : Nat.Coprime 2 p :=
    (Nat.coprime_primes Nat.prime_two hp.out).mpr (Ne.symm hodd)
  have hu : IsUnit (2 : ZMod p) := (ZMod.isUnit_iff_coprime 2 p).mpr hcop
  intro heq
  have hsum : a+a=0 := eq_neg_iff_add_eq_zero.mp heq
  have hmul : (2 : ZMod p)*a=(2 : ZMod p)*0 := by
    simpa only [two_mul, add_zero] using hsum
  exact ha (hu.mul_left_cancel hmul)

theorem third_witness_all_translates_unit {n p q : ℕ} [NeZero n]
    [Fact p.Prime] [Fact q.Prime] (hm : p*q ∣ n) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ p*q)
    (hpodd : p ≠ 2) (hqodd : q ≠ 2)
    (S : ZMod n → Prop) (hS : ∀ z, S z → S (-z))
    (v : ZMod n) (hv : S v) (hvunit : IsUnit v)
    (w : ZMod n) (hw : S w)
    (hwv : coordinates hm hc w ≠ coordinates hm hc v)
    (hwvi : coordinates hm hc w ≠ -(coordinates hm hc v)) :
    ∀ u : ZMod n, ∃ z, S z ∧ IsUnit (z-2*u) := by
  classical
  let π := coordinates hm hc
  let T := imageSupport π S
  have hT : ∀ x, T x → T (inversePoint Neg.neg Neg.neg x) := by
    intro x hx
    obtain ⟨z,hz,rfl⟩ := hx
    refine ⟨-z,hS z hz,?_⟩
    simp only [map_neg, inversePoint]
    rfl
  have hcoords := (isUnit_iff_coordinates hm hc hpr v).mp hvunit
  have ha := nonzero_ne_neg_prime hpodd hcoords.1
  have hb := nonzero_ne_neg_prime hqodd hcoords.2
  have hvT : T ((π v).1,(π v).2) := ⟨v,hv,rfl⟩
  have hwT : T (π w) := ⟨w,hw,rfl⟩
  have hwv' : π w ≠ ((π v).1,(π v).2) := hwv
  have hwvi' : π w ≠ (-(π v).1,-(π v).2) := hwvi
  have hno := third_point_excludes_cover Neg.neg Neg.neg
    (fun a => neg_neg a) (fun b => neg_neg b) T
    (fun x hx => hT x hx) (π v).1 (π v).2 ha hb hvT (π w) hwT hwv' hwvi'
  intro u
  apply Classical.byContradiction
  intro hn
  exact hno (2*(π u).1,2*(π u).2)
    ((no_unit_iff_cover hm hc hpr S u).mp hn)

theorem third_witness_all_translates_full_order {n p q : ℕ} [NeZero n]
    [Fact p.Prime] [Fact q.Prime] (hm : p*q ∣ n) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ p*q)
    (hpodd : p ≠ 2) (hqodd : q ≠ 2)
    (S : ZMod n → Prop) (hS : ∀ z, S z → S (-z))
    (v : ZMod n) (hv : S v) (hvunit : IsUnit v)
    (w : ZMod n) (hw : S w)
    (hwv : coordinates hm hc w ≠ coordinates hm hc v)
    (hwvi : coordinates hm hc w ≠ -(coordinates hm hc v)) :
    ∀ u : ZMod n, ∃ z, S z ∧ addOrderOf (z-2*u) = n := by
  intro u
  obtain ⟨z,hz,hu⟩ := third_witness_all_translates_unit hm hc hpr
    hpodd hqodd S hS v hv hvunit w hw hwv hwvi u
  exact ⟨z,hz,(isUnit_iff_full_addOrder (z-2*u)).mp hu⟩

noncomputable def coordinates513 : ZMod 513 →+* ZMod 3 × ZMod 19 :=
  coordinates (by decide : 3*19 ∣ 513) (by decide : Nat.Coprime 3 19)

theorem isUnit_sub_two_mod513_iff (z u : ZMod 513) :
    IsUnit (z-2*u) ↔
      (coordinates513 z).1 ≠ 2*(coordinates513 u).1 ∧
      (coordinates513 z).2 ≠ 2*(coordinates513 u).2 := by
  letI : Fact (Nat.Prime 3) := ⟨by decide⟩
  letI : Fact (Nat.Prime 19) := ⟨by decide⟩
  exact isUnit_sub_two_iff_coordinates
    (by decide : 3*19 ∣ 513) (by decide : Nat.Coprime 3 19)
    (prime_support_prime_powers 3 19 2 0) z u

theorem full_order_sub_two_mod513_iff (z u : ZMod 513) :
    addOrderOf (z-2*u) = 513 ↔
      (coordinates513 z).1 ≠ 2*(coordinates513 u).1 ∧
      (coordinates513 z).2 ≠ 2*(coordinates513 u).2 :=
  (isUnit_iff_full_addOrder (z-2*u)).symm.trans (isUnit_sub_two_mod513_iff z u)

theorem third_witness_mod513
    (S : ZMod 513 → Prop) (hS : ∀ z, S z → S (-z))
    (v : ZMod 513) (hv : S v) (hvunit : IsUnit v)
    (w : ZMod 513) (hw : S w)
    (hwv : coordinates513 w ≠ coordinates513 v)
    (hwvi : coordinates513 w ≠ -(coordinates513 v)) :
    ∀ u : ZMod 513, ∃ z, S z ∧ addOrderOf (z-2*u) = 513 := by
  letI : Fact (Nat.Prime 3) := ⟨by decide⟩
  letI : Fact (Nat.Prime 19) := ⟨by decide⟩
  exact third_witness_all_translates_full_order
    (by decide : 3*19 ∣ 513) (by decide : Nat.Coprime 3 19)
    (prime_support_prime_powers 3 19 2 0)
    (by decide : 3 ≠ 2) (by decide : 19 ≠ 2)
    S hS v hv hvunit w hw hwv hwvi

#print axioms coprime_prime_support_reduction
#print axioms isUnit_quotient_iff
#print axioms isUnit_iff_full_addOrder
#print axioms prime_support_prime_powers
#print axioms product_dvd_prime_powers
#print axioms isUnit_mod513_iff_mod57
#print axioms isUnit_iff_coordinates
#print axioms isUnit_sub_two_iff_coordinates
#print axioms no_unit_iff_cover
#print axioms nonzero_ne_neg_prime
#print axioms third_witness_all_translates_unit
#print axioms third_witness_all_translates_full_order
#print axioms isUnit_sub_two_mod513_iff
#print axioms full_order_sub_two_mod513_iff
#print axioms third_witness_mod513

end PaperA.CyclicSupport
