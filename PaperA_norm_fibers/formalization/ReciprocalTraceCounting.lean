import ReciprocalTraceSupport
import Mathlib.Algebra.CharP.Two
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Lean.Elab.Tactic.Omega

/-!
# Exact two-to-one reciprocal-trace counting

The normalized trace is the actual field expression `(γ + γ⁻¹) / h²`.
For nonzero inputs and `h ≠ 0`, equality of two such traces forces the
inputs to be equal or inverse.  Exact-order elements in characteristic two
are not fixed by inversion when their order is greater than one.  Therefore
every attained primitive trace has exactly two primitive preimages.

The final finite-field cardinality identity allows any predicate that depends
only on this trace, including the paper's shifted full-order predicate.
It counts the `γ` parameters.  The separate rational substitution
`a = c / (1 + γ)` and its order-component equivalence are not formalized here.
-/

namespace PaperA.ReciprocalTraceCounting

open scoped BigOperators

abbrev normalizedTrace {L : Type*} [Field L] (γ h : L) : L :=
  PaperA.ReciprocalTrace.reciprocalTrace γ h

lemma normalizedTrace_inv {L : Type*} [Field L] (γ h : L) :
    normalizedTrace γ⁻¹ h = normalizedTrace γ h := by
  simp only [normalizedTrace, PaperA.ReciprocalTrace.reciprocalTrace, inv_inv, add_comm]

lemma normalizedTrace_eq_iff {L : Type*} [Field L] {δ γ h : L}
    (hδ : δ ≠ 0) (hγ : γ ≠ 0) (hh : h ≠ 0) :
    normalizedTrace δ h = normalizedTrace γ h ↔ δ = γ ∨ δ = γ⁻¹ := by
  constructor
  · intro heq
    have hs : δ + δ⁻¹ = γ + γ⁻¹ :=
      (div_left_inj' (pow_ne_zero 2 hh)).mp heq
    have hf : (δ - γ) * (δ * γ - 1) = 0 := by
      field_simp [hδ, hγ] at hs
      linear_combination hs
    rcases mul_eq_zero.mp hf with h | h
    · exact Or.inl (sub_eq_zero.mp h)
    · exact Or.inr (eq_inv_of_mul_eq_one_left (sub_eq_zero.mp h))
  · rintro (rfl | rfl)
    · rfl
    · exact normalizedTrace_inv γ h

lemma orderOf_inverse_field {L : Type*} [Field L] (γ : L) :
    orderOf γ⁻¹ = orderOf γ := by
  rw [orderOf_eq_orderOf_iff]
  intro n
  simp only [inv_pow, inv_eq_one]

lemma nonzero_of_exact_order {L : Type*} [Field L] {γ : L} {B : ℕ}
    (hB : B ≠ 0) (hγ : orderOf γ = B) : γ ≠ 0 := by
  intro hz
  apply hB
  simpa only [hz, orderOf_zero] using hγ.symm

lemma not_self_inverse_of_exact_order {L : Type*} [Field L] [CharP L 2]
    {γ : L} {B : ℕ} (hB : 1 < B) (hγ : orderOf γ = B) : γ ≠ γ⁻¹ := by
  intro hi
  rcases self_eq_inv₀.mp hi with h | h | h
  · have h1 : γ = 1 := by simpa only [CharTwo.neg_eq] using h
    have ho : B = 1 := by simpa only [h1, orderOf_one] using hγ.symm
    omega
  · exact nonzero_of_exact_order (by omega) hγ h
  · have ho : B = 1 := by simpa only [h, orderOf_one] using hγ.symm
    omega

noncomputable def primitiveFiber {L : Type*} [Field L] [Fintype L]
    (B : ℕ) (h z : L) : Finset L := by
  classical
  exact Finset.univ.filter fun δ => orderOf δ = B ∧ normalizedTrace δ h = z

theorem primitive_fiber_eq_pair {L : Type*} [Field L] [Fintype L] [DecidableEq L]
    {B : ℕ} {γ h : L} (hB : B ≠ 0) (hγ : orderOf γ = B) (hh : h ≠ 0) :
    primitiveFiber B h (normalizedTrace γ h) = {γ, γ⁻¹} := by
  classical
  ext δ
  simp only [primitiveFiber, Finset.mem_filter, Finset.mem_univ, true_and,
    Finset.mem_insert, Finset.mem_singleton]
  constructor
  · rintro ⟨hδ, heq⟩
    exact (normalizedTrace_eq_iff (nonzero_of_exact_order hB hδ)
      (nonzero_of_exact_order hB hγ) hh).mp heq
  · rintro (rfl | rfl)
    · exact ⟨hγ, rfl⟩
    · exact ⟨(orderOf_inverse_field γ).trans hγ, normalizedTrace_inv γ h⟩

theorem primitive_fiber_card_two {L : Type*} [Field L] [Fintype L]
    [CharP L 2] {B : ℕ} {γ h : L}
    (hB : 1 < B) (hγ : orderOf γ = B) (hh : h ≠ 0) :
    (primitiveFiber B h (normalizedTrace γ h)).card = 2 := by
  classical
  rw [primitive_fiber_eq_pair (by omega) hγ hh]
  exact Finset.card_pair (not_self_inverse_of_exact_order hB hγ)

theorem support_fiber_card_two {L : Type*} [Field L] [Fintype L]
    [CharP L 2] {t : ℕ} {h z : L} (ht : 2 ≤ t) (hh : h ≠ 0)
    (hz : z ∈ PaperA.ReciprocalTrace.support t h) :
    (primitiveFiber (t ^ 2 + 1) h z).card = 2 := by
  have hp : 0 < t ^ 2 := pow_pos (by omega : 0 < t) 2
  have hB : 1 < t ^ 2 + 1 := by omega
  rcases hz with ⟨_, γ, hγ, rfl⟩
  exact primitive_fiber_card_two hB hγ hh

noncomputable def filteredSource {L : Type*} [Field L] [Fintype L]
    (t : ℕ) (h : L) (P : L → Prop) : Finset L := by
  classical
  exact Finset.univ.filter fun γ => orderOf γ = t ^ 2 + 1 ∧
    normalizedTrace γ h ^ (t + 1) = 1 ∧ P (normalizedTrace γ h)

noncomputable def filteredSupport {L : Type*} [Field L] [Fintype L]
    (t : ℕ) (h : L) (P : L → Prop) : Finset L := by
  classical
  exact Finset.univ.filter fun z => z ∈ PaperA.ReciprocalTrace.support t h ∧ P z

lemma mem_filteredSource {L : Type*} [Field L] [Fintype L]
    (t : ℕ) (h : L) (P : L → Prop) (γ : L) :
    γ ∈ filteredSource t h P ↔ orderOf γ = t ^ 2 + 1 ∧
      normalizedTrace γ h ^ (t + 1) = 1 ∧ P (normalizedTrace γ h) := by
  classical
  simp only [filteredSource, Finset.mem_filter, Finset.mem_univ, true_and]

lemma mem_filteredSupport {L : Type*} [Field L] [Fintype L]
    (t : ℕ) (h : L) (P : L → Prop) (z : L) :
    z ∈ filteredSupport t h P ↔ z ∈ PaperA.ReciprocalTrace.support t h ∧ P z := by
  classical
  simp only [filteredSupport, Finset.mem_filter, Finset.mem_univ, true_and]

lemma filtered_fiber_eq_primitiveFiber {L : Type*} [Field L] [Fintype L] [DecidableEq L]
    {t : ℕ} {h z : L} {P : L → Prop} (hz : z ∈ filteredSupport t h P) :
    (filteredSource t h P).filter (fun γ => normalizedTrace γ h = z) =
      primitiveFiber (t ^ 2 + 1) h z := by
  classical
  have hzp := (mem_filteredSupport t h P z).mp hz
  ext γ
  simp only [Finset.mem_filter, mem_filteredSource, primitiveFiber,
    Finset.mem_univ, true_and]
  constructor
  · rintro ⟨⟨ho, _, _⟩, heq⟩
    exact ⟨ho, heq⟩
  · rintro ⟨ho, heq⟩
    refine ⟨⟨ho, ?_, ?_⟩, heq⟩
    · rw [heq]
      exact hzp.1.1
    · rw [heq]
      exact hzp.2

lemma filtered_source_maps_to_support {L : Type*} [Field L] [Fintype L]
    (t : ℕ) (h : L) (P : L → Prop) :
    (filteredSource t h P : Set L).MapsTo (fun γ => normalizedTrace γ h)
      (filteredSupport t h P : Set L) := by
  intro γ hγ
  obtain ⟨ho, hn, hP⟩ := (mem_filteredSource t h P γ).mp hγ
  apply (mem_filteredSupport t h P (normalizedTrace γ h)).mpr
  exact ⟨⟨hn, γ, ho, rfl⟩, hP⟩

/-- The exact two-to-one counting identity for every filter that depends only
on the normalized reciprocal trace.  The fiber size is derived above.
-/
theorem filtered_source_card_eq_two_mul_support_card
    {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {t : ℕ} {h : L} (ht : 2 ≤ t) (hh : h ≠ 0) (P : L → Prop) :
    (filteredSource t h P).card = 2 * (filteredSupport t h P).card := by
  classical
  calc
    (filteredSource t h P).card =
        ∑ z ∈ filteredSupport t h P,
          ((filteredSource t h P).filter (fun γ => normalizedTrace γ h = z)).card :=
      Finset.card_eq_sum_card_fiberwise (filtered_source_maps_to_support t h P)
    _ = ∑ _z ∈ filteredSupport t h P, 2 := by
      apply Finset.sum_congr rfl
      intro z hz
      rw [filtered_fiber_eq_primitiveFiber hz]
      exact support_fiber_card_two ht hh ((mem_filteredSupport t h P z).mp hz).1
    _ = 2 * (filteredSupport t h P).card := by simp only [Finset.sum_const,
      smul_eq_mul, Nat.mul_comm]

/-- The order filter used on the right-hand side of the paper's support
counting formula.  This theorem counts the `γ` parameters; it does not yet
identify them with the original `a=c/(1+γ)` population.
-/
theorem primitive_order_filter_count
    {L : Type*} [Field L] [Fintype L] [CharP L 2]
    {t : ℕ} {h : L} (ht : 2 ≤ t) (hh : h ≠ 0) (u : L) :
    (filteredSource t h (fun z => orderOf (z * (u⁻¹) ^ 2) = t + 1)).card =
      2 * (filteredSupport t h (fun z => orderOf (z * (u⁻¹) ^ 2) = t + 1)).card :=
  filtered_source_card_eq_two_mul_support_card ht hh _

/-- The binary parameter `t = 2^s`, with `s ≥ 1`, satisfies the threshold
required by the exact two-to-one counting theorem.
-/
theorem binary_filtered_source_card_eq_two_mul_support_card
    {L : Type*} [Field L] [Fintype L] [CharP L 2]
    (s : ℕ) (hs : 1 ≤ s) {h : L} (hh : h ≠ 0) (P : L → Prop) :
    (filteredSource (2 ^ s) h P).card =
      2 * (filteredSupport (2 ^ s) h P).card := by
  cases s with
  | zero => omega
  | succ s =>
    have hp : 0 < 2 ^ s := pow_pos (by decide : 0 < (2 : ℕ)) s
    have ht : 2 ≤ 2 ^ (s + 1) := by rw [pow_succ]; omega
    exact filtered_source_card_eq_two_mul_support_card ht hh P

end PaperA.ReciprocalTraceCounting

#print axioms PaperA.ReciprocalTraceCounting.normalizedTrace
#print axioms PaperA.ReciprocalTraceCounting.normalizedTrace_inv
#print axioms PaperA.ReciprocalTraceCounting.normalizedTrace_eq_iff
#print axioms PaperA.ReciprocalTraceCounting.orderOf_inverse_field
#print axioms PaperA.ReciprocalTraceCounting.nonzero_of_exact_order
#print axioms PaperA.ReciprocalTraceCounting.not_self_inverse_of_exact_order
#print axioms PaperA.ReciprocalTraceCounting.primitiveFiber
#print axioms PaperA.ReciprocalTraceCounting.primitive_fiber_eq_pair
#print axioms PaperA.ReciprocalTraceCounting.primitive_fiber_card_two
#print axioms PaperA.ReciprocalTraceCounting.support_fiber_card_two
#print axioms PaperA.ReciprocalTraceCounting.filteredSource
#print axioms PaperA.ReciprocalTraceCounting.filteredSupport
#print axioms PaperA.ReciprocalTraceCounting.mem_filteredSource
#print axioms PaperA.ReciprocalTraceCounting.mem_filteredSupport
#print axioms PaperA.ReciprocalTraceCounting.filtered_fiber_eq_primitiveFiber
#print axioms PaperA.ReciprocalTraceCounting.filtered_source_maps_to_support
#print axioms PaperA.ReciprocalTraceCounting.filtered_source_card_eq_two_mul_support_card
#print axioms PaperA.ReciprocalTraceCounting.primitive_order_filter_count
#print axioms PaperA.ReciprocalTraceCounting.binary_filtered_source_card_eq_two_mul_support_card
