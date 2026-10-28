import Mathlib.FieldTheory.Finite.Basic
import Mathlib.GroupTheory.OrderOfElement

/-!
# Reciprocal-trace support and Frobenius

For a finite base field `K` of cardinality `t`, and any field extension `L/K`,
the `t`-power Frobenius fixes the image of `K`.  It sends the reciprocal trace
`(γ + γ⁻¹) / h²` to its `t`-th power.  On the norm-one locus `z^(t+1)=1`,
that power equals `z⁻¹`.  Moreover `γ ↦ γ^t` preserves the exact order `t²+1`.
These facts construct a new witness for inverse membership of the support.

This is the finite-field interface behind `T_h = T_h⁻¹` in the paper.  The
proof works in every characteristic; the binary specialization uses
`Fintype.card K = 2^s`.  It does not formalize the geometric character bound,
the two-preimage counting formula, or the whole trace classification.
-/

namespace PaperA.ReciprocalTrace

def reciprocalTrace {L : Type*} [Field L] (γ h : L) : L :=
  (γ + γ⁻¹) / h ^ 2

def support {L : Type*} [Field L] (t : ℕ) (h : L) : Set L :=
  {z | z ^ (t + 1) = 1 ∧
    ∃ γ : L, orderOf γ = t ^ 2 + 1 ∧ z = reciprocalTrace γ h}

lemma square_add_one_coprime (t : ℕ) : Nat.Coprime (t ^ 2 + 1) t := by
  rw [pow_two]
  exact (Nat.coprime_mul_left_add_left 1 t t).2 (Nat.coprime_one_left t)

lemma orderOf_pow_preserved {L : Type*} [Field L] {t : ℕ} {γ : L}
    (hγ : orderOf γ = t ^ 2 + 1) : orderOf (γ ^ t) = t ^ 2 + 1 := by
  have hc : Nat.Coprime (orderOf γ) t := by
    rw [hγ]
    exact square_add_one_coprime t
  exact hc.orderOf_pow.trans hγ

lemma pow_eq_inverse {L : Type*} [Field L] {z : L} {t : ℕ}
    (hz : z ^ (t + 1) = 1) : z ^ t = z⁻¹ := by
  apply eq_inv_of_mul_eq_one_left
  simpa [pow_succ] using hz

/-- A root of the `t+1` norm-one equation lies in the quadratic Frobenius
fixed locus.  No prior subfield-membership or inverse-closure assumption is used.
-/
lemma norm_one_quadratic_fixed {L : Type*} [Field L] {z : L} {t : ℕ}
    (hz : z ^ (t + 1) = 1) : z ^ (t ^ 2) = z := by
  calc
    z ^ (t ^ 2) = (z ^ t) ^ t := by rw [pow_two, pow_mul]
    _ = (z⁻¹) ^ t := by rw [pow_eq_inverse hz]
    _ = (z ^ t)⁻¹ := inv_pow z t
    _ = z := by rw [pow_eq_inverse hz, inv_inv]

/-- An element of exact order `t²+1` lies in the quartic Frobenius fixed
locus.  In the paper's finite field this is the expected ambient extension.
-/
lemma exact_order_quartic_fixed {L : Type*} [Field L] {γ : L} {t : ℕ}
    (hγ : orderOf γ = t ^ 2 + 1) : γ ^ (t ^ 4) = γ := by
  have hn : γ ^ (t ^ 2 + 1) = 1 := by
    rw [← hγ]
    exact pow_orderOf_eq_one γ
  simpa only [← pow_mul, Nat.reduceMul] using norm_one_quadratic_fixed hn

section FiniteBase

variable (K L : Type*) [Field K] [Fintype K] [Field L] [Algebra K L]

/-- The actual finite-base-field Frobenius commutes with the reciprocal-trace
expression; its fixation of the base-field parameter is supplied by `Algebra`.
-/
lemma frobenius_reciprocalTrace (γ : L) (h : K) :
    reciprocalTrace (γ ^ Fintype.card K) (algebraMap K L h) =
      reciprocalTrace γ (algebraMap K L h) ^ Fintype.card K := by
  let σ := FiniteField.frobeniusAlgHom K L
  have hfix : σ (algebraMap K L h) = algebraMap K L h := σ.commutes h
  change reciprocalTrace (σ γ) (algebraMap K L h) =
    σ (reciprocalTrace γ (algebraMap K L h))
  simp only [reciprocalTrace, map_div₀, map_add, map_inv₀, map_pow, hfix]

/-- On the `t+1` norm-one locus, the transformed reciprocal trace is its inverse.
The norm-one condition is a support-membership condition, not inverse closure.
-/
lemma transformed_trace_eq_inverse (γ : L) (h : K)
    (hz : reciprocalTrace γ (algebraMap K L h) ^ (Fintype.card K + 1) = 1) :
    reciprocalTrace (γ ^ Fintype.card K) (algebraMap K L h) =
      (reciprocalTrace γ (algebraMap K L h))⁻¹ := by
  exact (frobenius_reciprocalTrace K L γ h).trans (pow_eq_inverse hz)

/-- Raising the original witness to the cardinality of `K` witnesses inverse
membership in the same support, with its exact order proved rather than assumed.
-/
theorem inv_mem_support (h : K) {z : L}
    (hz : z ∈ support (Fintype.card K) (algebraMap K L h)) :
    z⁻¹ ∈ support (Fintype.card K) (algebraMap K L h) := by
  rcases hz with ⟨hzpow, γ, hγ, hzγ⟩
  refine ⟨?_, γ ^ Fintype.card K, orderOf_pow_preserved hγ, ?_⟩
  · simp only [inv_pow, hzpow, inv_one]
  · calc
      z⁻¹ = z ^ Fintype.card K := (pow_eq_inverse hzpow).symm
      _ = reciprocalTrace γ (algebraMap K L h) ^ Fintype.card K := by rw [hzγ]
      _ = reciprocalTrace (γ ^ Fintype.card K) (algebraMap K L h) :=
        (frobenius_reciprocalTrace K L γ h).symm

theorem inv_mem_support_iff (h : K) (z : L) :
    z⁻¹ ∈ support (Fintype.card K) (algebraMap K L h) ↔
      z ∈ support (Fintype.card K) (algebraMap K L h) := by
  constructor
  · intro hz
    simpa only [inv_inv] using inv_mem_support K L h hz
  · exact inv_mem_support K L h

/-- Set equality expressing inverse closure, with explicit inverse-image
witnesses and without assuming any closure property of the original support.
-/
theorem inverse_image_support (h : K) :
    (fun z : L => z⁻¹) '' support (Fintype.card K) (algebraMap K L h) =
      support (Fintype.card K) (algebraMap K L h) := by
  ext z
  constructor
  · rintro ⟨y, hy, rfl⟩
    exact inv_mem_support K L h hy
  · intro hz
    exact ⟨z⁻¹, inv_mem_support K L h hz, inv_inv z⟩

/-- The paper's binary parameter `t=2^s` is connected to a genuine finite
base field by its cardinality, not an abstract assumed Frobenius identity.
-/
theorem binary_inverse_image_support (s : ℕ)
    (hcard : Fintype.card K = 2 ^ s) (h : K) :
    (fun z : L => z⁻¹) '' support (2 ^ s) (algebraMap K L h) =
      support (2 ^ s) (algebraMap K L h) := by
  simpa only [hcard] using inverse_image_support K L h

end FiniteBase

end PaperA.ReciprocalTrace

#print axioms PaperA.ReciprocalTrace.square_add_one_coprime
#print axioms PaperA.ReciprocalTrace.orderOf_pow_preserved
#print axioms PaperA.ReciprocalTrace.pow_eq_inverse
#print axioms PaperA.ReciprocalTrace.norm_one_quadratic_fixed
#print axioms PaperA.ReciprocalTrace.exact_order_quartic_fixed
#print axioms PaperA.ReciprocalTrace.frobenius_reciprocalTrace
#print axioms PaperA.ReciprocalTrace.transformed_trace_eq_inverse
#print axioms PaperA.ReciprocalTrace.inv_mem_support
#print axioms PaperA.ReciprocalTrace.inv_mem_support_iff
#print axioms PaperA.ReciprocalTrace.inverse_image_support
#print axioms PaperA.ReciprocalTrace.binary_inverse_image_support
