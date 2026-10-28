import Mathlib.FieldTheory.Finite.Trace
import RelativeTraceTransfer

/-!
Identification of the power/root count with the named Algebra.norm and
Algebra.trace count in a genuine quadratic-quadratic finite-field tower.
The trace population below is the manuscript's M_c, rather than a renamed
gamma population. Geometric estimates and finite certificates are separate.
-/

namespace PaperA.NamedNormTraceTransfer

open PaperA.RelativeTraceTransfer

variable (K E L : Type*) [Field K] [Fintype K] [Field E] [Fintype E]
  [Field L] [Fintype L] [Algebra K E] [Algebra E L] [Algebra K L]
  [IsScalarTower K E L]

lemma quadratic_card {s : ℕ} (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) : Fintype.card E = t s^2 := by
  rw [Module.card_eq_pow_finrank (K := K), hKE, hcard]

omit [Fintype K] [Fintype E] [Fintype L] in
lemma quartic_rank (hKE : Module.finrank K E = 2)
    (hEL : Module.finrank E L = 2) : Module.finrank K L = 4 := by
  rw [← Module.finrank_mul_finrank K E L, hKE, hEL]

lemma norm_power_quadratic {s : ℕ} (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (u : E) :
    algebraMap K E (Algebra.norm K u) = u^A s := by
  rw [FiniteField.algebraMap_norm_eq_pow_sum, hKE, Nat.card_eq_fintype_card, hcard]
  congr 1
  simp [Finset.sum_range_succ, A, Nat.add_comm]

omit [Fintype E] in
lemma norm_power_quartic {s : ℕ} (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2) (a : L) :
    algebraMap K L (Algebra.norm K a) = a^d s := by
  rw [FiniteField.algebraMap_norm_eq_pow_sum, quartic_rank K E L hKE hEL,
    Nat.card_eq_fintype_card, hcard]
  congr 1
  norm_num [Finset.sum_range_succ, d, A, B]
  ring

omit [Algebra K L] [IsScalarTower K E L] in
lemma trace_power_quadratic {s : ℕ} (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2) (a : L) :
    algebraMap E L (Algebra.trace E L a) = a+a^(t s^2) := by
  rw [FiniteField.algebraMap_trace_eq_sum_pow, hEL, Nat.card_eq_fintype_card,
    quadratic_card K E hcard hKE]
  simp [Finset.sum_range_succ]

omit [Fintype E] in
lemma norm_one_iff_power {s : ℕ} (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2) (a : L) :
    Algebra.norm K a = 1 ↔ a^d s = 1 := by
  rw [← norm_power_quartic K E L hcard hKE hEL]
  exact ((algebraMap K L).injective.eq_iff' (map_one (algebraMap K L))).symm

omit [Algebra K L] [IsScalarTower K E L] in
lemma trace_eq_iff_power {s : ℕ} (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2) (a : L) (c : E) :
    Algebra.trace E L a = c ↔ a+a^(t s^2) = algebraMap E L c := by
  rw [← trace_power_quadratic K E L hcard hKE hEL]
  exact (algebraMap E L).injective.eq_iff.symm

noncomputable def primitiveElements (s : ℕ) (c : E) : Finset L := by
  classical
  exact Finset.univ.filter fun a => Algebra.norm K a = 1 ∧
    orderOf a = d s ∧ Algebra.trace E L a = c

noncomputable def M (s : ℕ) (c : E) : ℕ := (primitiveElements K E L s c).card

theorem named_M_eq_power_M {s : ℕ} (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2) (c : E) :
    M K E L s c = PaperA.RelativeTraceTransfer.M s (algebraMap E L c) := by
  classical
  unfold M PaperA.RelativeTraceTransfer.M
  congr 1
  ext a
  simp only [primitiveElements, PaperA.RelativeTraceTransfer.primitiveElements,
    Finset.mem_filter, Finset.mem_univ, true_and]
  rw [norm_one_iff_power K E L hcard hKE hEL,
    trace_eq_iff_power K E L hcard hKE hEL]

theorem named_M_eq_two_mul_support_count [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2)
    (c : E) (hc : c ≠ 0) :
    M K E L s c = 2 * (PaperA.ReciprocalTraceCounting.filteredSupport
      (t s) (algebraMap E L c) (fun w => orderOf w = A s)).card := by
  rw [named_M_eq_power_M K E L hcard hKE hEL]
  apply M_eq_two_mul_support_count hs ((map_ne_zero (algebraMap E L)).mpr hc)
  rw [← quadratic_card K E hcard hKE]
  exact (FiniteField.frobeniusAlgHom E L).commutes c

theorem named_M_shifted_support_count [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2)
    (h : K) (hh : h ≠ 0) (u : E) (hu : Algebra.norm K u = 1) :
    M K E L s (algebraMap K E h * u) =
      2 * (PaperA.ReciprocalTraceCounting.filteredSupport
        (t s) (algebraMap K L h)
        (fun z => orderOf (z*((algebraMap E L u)⁻¹)^2) = A s)).card := by
  have huE : u^A s = 1 := by
    have hnorm := norm_power_quadratic K E hcard hKE u
    rw [hu, map_one] at hnorm
    exact hnorm.symm
  have huL : (algebraMap E L u)^A s = 1 := by
    rw [← map_pow, huE, map_one]
  rw [named_M_eq_power_M K E L hcard hKE hEL, map_mul,
    ← IsScalarTower.algebraMap_apply K E L]
  exact finite_base_M_shifted_support_count K L hs hcard h hh _ huL

theorem named_M_shifted_parameter_count [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2)
    (h : K) (hh : h ≠ 0) (u : E) (hu : Algebra.norm K u = 1) :
    M K E L s (algebraMap K E h*u) =
      (PaperA.ReciprocalTraceCounting.filteredSource
        (t s) (algebraMap K L h)
        (fun z => orderOf (z*((algebraMap E L u)⁻¹)^2) = A s)).card := by
  rw [named_M_shifted_support_count K E L hs hcard hKE hEL h hh u hu,
    PaperA.ReciprocalTraceCounting.filtered_source_card_eq_two_mul_support_card
      (t_two_le hs) ((map_ne_zero (algebraMap K L)).mpr hh)]

theorem named_M_zero [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2) :
    M K E L s 0 = 0 := by
  rw [named_M_eq_power_M K E L hcard hKE hEL, map_zero]
  exact M_zero hs

theorem named_M_zero_iff_empty_support [CharP L 2]
    {s : ℕ} (hs : 1 ≤ s) (hcard : Fintype.card K = t s)
    (hKE : Module.finrank K E = 2) (hEL : Module.finrank E L = 2)
    (h : K) (hh : h ≠ 0) (u : E) (hu : Algebra.norm K u = 1) :
    M K E L s (algebraMap K E h*u) = 0 ↔
      PaperA.ReciprocalTraceCounting.filteredSupport
        (t s) (algebraMap K L h)
        (fun z => orderOf (z*((algebraMap E L u)⁻¹)^2) = A s) = ∅ := by
  rw [named_M_shifted_support_count K E L hs hcard hKE hEL h hh u hu]
  simp only [Nat.mul_eq_zero, OfNat.ofNat_ne_zero, false_or, Finset.card_eq_zero]

end PaperA.NamedNormTraceTransfer
