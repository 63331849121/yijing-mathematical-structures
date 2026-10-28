import Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots
import ReciprocalTraceSupport
import MultiplicativeSupport
import ReciprocalTraceCounting

/-!
The actual finite-field root subgroup used for the norm-one support.
The cyclic group and its size are derived from field cardinality, rather than
assumed as an exponent-model interface. Full relative-trace counting is separate.
-/

namespace PaperA.NormOneSupportBridge

open PaperA.ReciprocalTrace

theorem roots_card_of_dvd (L : Type*) [Field L] [Fintype L]
    (n : ℕ) [NeZero n] (hd : n ∣ Fintype.card L - 1) :
    Fintype.card (rootsOfUnity n L) = n := by
  obtain ⟨g, hg⟩ := IsCyclic.exists_ofOrder_eq_natCard (α := Lˣ)
  have horder : orderOf g = Fintype.card L - 1 := by
    simpa only [Nat.card_units, Nat.card_eq_fintype_card] using hg
  have hne : orderOf g ≠ 0 := (orderOf_pos g).ne'
  have hd' : n ∣ orderOf g := by rw [horder]; exact hd
  have hprimitive : IsPrimitiveRoot (g ^ (orderOf g / n)) n :=
    IsPrimitiveRoot.iff_orderOf.mpr (orderOf_pow_orderOf_div hne hd')
  exact hprimitive.card_rootsOfUnity'

theorem plus_one_dvd_quartic_sub_one {t : ℕ} (ht : 1 ≤ t) :
    t+1 ∣ t^4-1 := by
  cases t with
  | zero => omega
  | succ k =>
    refine ⟨k*((k+1)^2+1), ?_⟩
    have h : (k+1)^4 = (k+1+1)*(k*((k+1)^2+1))+1 := by ring
    simp only [h, Nat.add_sub_cancel]

theorem norm_group_card (L : Type*) [Field L] [Fintype L]
    {t : ℕ} (ht : 1 ≤ t) (hcard : Fintype.card L = t^4) :
    Fintype.card (rootsOfUnity (t+1) L) = t+1 := by
  apply roots_card_of_dvd
  rw [hcard]
  exact plus_one_dvd_quartic_sub_one ht

def rootValue {L : Type*} [Field L] {n : ℕ} (z : rootsOfUnity n L) : L :=
  ((z : Lˣ) : L)

theorem rootValue_injective {L : Type*} [Field L] {n : ℕ} :
    Function.Injective (rootValue (L := L) (n := n)) :=
  rootsOfUnity.coe_injective

theorem rootValue_inv {L : Type*} [Field L] {n : ℕ} (z : rootsOfUnity n L) :
    rootValue z⁻¹ = (rootValue z)⁻¹ := by
  simp [rootValue]

theorem rootValue_orderOf {L : Type*} [Field L] {n : ℕ} (z : rootsOfUnity n L) :
    orderOf (rootValue z) = orderOf z := by
  exact orderOf_injective
    ((Units.coeHom L).comp (rootsOfUnity n L).subtype) rootValue_injective z

def groupSupport {K L : Type*} [Field K] [Fintype K] [Field L] [Algebra K L]
    (h : K) (z : rootsOfUnity (Fintype.card K+1) L) : Prop :=
  rootValue z ∈ support (Fintype.card K) (algebraMap K L h)

theorem groupSupport_inverse {K L : Type*} [Field K] [Fintype K]
    [Field L] [Algebra K L] (h : K)
    (z : rootsOfUnity (Fintype.card K+1) L) (hz : groupSupport h z) :
    groupSupport h z⁻¹ := by
  change rootValue z⁻¹ ∈ support _ _
  rw [rootValue_inv]
  exact inv_mem_support K L h hz

theorem rootValue_mul_inv_sq {L : Type*} [Field L] {n : ℕ}
    (z u : rootsOfUnity n L) :
    rootValue (z * u ^ (-2 : ℤ)) = rootValue z * rootValue u ^ (-2 : ℤ) := by
  simp [rootValue]

theorem finite_base_norm_group_card (K L : Type*)
    [Field K] [Fintype K] [Field L] [Fintype L]
    (hcard : Fintype.card L = (Fintype.card K)^4) :
    Fintype.card (rootsOfUnity (Fintype.card K+1) L) = Fintype.card K+1 :=
  norm_group_card L Fintype.card_pos hcard

theorem field_support_all_translates {K L : Type*}
    [Field K] [Fintype K] [Field L] [Fintype L] [Algebra K L]
    (hcard : Fintype.card L = (Fintype.card K)^4)
    {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    (hm : p*q ∣ Fintype.card K+1) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ Fintype.card K+1 → r ∣ p*q)
    (hpodd : p ≠ 2) (hqodd : q ≠ 2) (h : K)
    (v : rootsOfUnity (Fintype.card K+1) L) (hv : groupSupport h v)
    (hvorder : orderOf v = Fintype.card K+1)
    (w : rootsOfUnity (Fintype.card K+1) L) (hw : groupSupport h w)
    (hwv : PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc w ≠
      PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc v)
    (hwvi : PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc w ≠
      -(PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc v)) :
    ∀ u : rootsOfUnity (Fintype.card K+1) L,
      ∃ z, groupSupport h z ∧ orderOf (z * u ^ (-2 : ℤ)) = Fintype.card K+1 := by
  exact PaperA.MultiplicativeSupport.third_witness_all_translates
    (finite_base_norm_group_card K L hcard) hm hc hpr hpodd hqodd
    (groupSupport h) (groupSupport_inverse h) v hv hvorder w hw hwv hwvi

noncomputable def filteredGroupSupport {K L : Type*}
    [Field K] [Fintype K] [Field L] [Algebra K L]
    (h : K) (P : L → Prop) : Finset (rootsOfUnity (Fintype.card K+1) L) := by
  classical
  exact Finset.univ.filter fun z => groupSupport h z ∧ P (rootValue z)

theorem group_support_count_eq_field_support_count {K L : Type*}
    [Field K] [Fintype K] [Field L] [Fintype L] [Algebra K L]
    (h : K) (P : L → Prop) :
    (filteredGroupSupport h P).card =
      (PaperA.ReciprocalTraceCounting.filteredSupport
        (Fintype.card K) (algebraMap K L h) P).card := by
  classical
  apply Finset.card_bij (fun z _ => rootValue z)
  · intro z hz
    exact (PaperA.ReciprocalTraceCounting.mem_filteredSupport _ _ _ _).mpr
      (by simpa only [filteredGroupSupport, Finset.mem_filter,
        Finset.mem_univ, true_and, groupSupport] using hz)
  · intro a _ b _ hab
    exact rootValue_injective hab
  · intro z hz
    have hp := (PaperA.ReciprocalTraceCounting.mem_filteredSupport _ _ _ _).mp hz
    let zz : rootsOfUnity (Fintype.card K+1) L := rootsOfUnity.mkOfPowEq z hp.1.1
    refine ⟨zz, ?_, rfl⟩
    simp only [filteredGroupSupport, Finset.mem_filter, Finset.mem_univ, true_and]
    change (z ∈ support (Fintype.card K) (algebraMap K L h)) ∧ P z
    exact hp

theorem parameter_count_eq_two_mul_group_support_count {K L : Type*}
    [Field K] [Fintype K] [Field L] [Fintype L] [Algebra K L] [CharP L 2]
    (h : K) (hh : h ≠ 0) (P : L → Prop) :
    (PaperA.ReciprocalTraceCounting.filteredSource
      (Fintype.card K) (algebraMap K L h) P).card =
      2 * (filteredGroupSupport h P).card := by
  rw [group_support_count_eq_field_support_count]
  apply PaperA.ReciprocalTraceCounting.filtered_source_card_eq_two_mul_support_card
  · exact Fintype.one_lt_card
  · exact (map_ne_zero (algebraMap K L)).mpr hh

theorem parameter_count_positive_of_group_witness {K L : Type*}
    [Field K] [Fintype K] [Field L] [Fintype L] [Algebra K L] [CharP L 2]
    (h : K) (hh : h ≠ 0) (P : L → Prop)
    (z : rootsOfUnity (Fintype.card K+1) L) (hz : groupSupport h z)
    (hP : P (rootValue z)) :
    0 < (PaperA.ReciprocalTraceCounting.filteredSource
      (Fintype.card K) (algebraMap K L h) P).card := by
  classical
  rw [parameter_count_eq_two_mul_group_support_count h hh P]
  have hc : 0 < (filteredGroupSupport h P).card := by
    apply Finset.card_pos.mpr
    refine ⟨z, ?_⟩
    simpa only [filteredGroupSupport, Finset.mem_filter, Finset.mem_univ,
      true_and] using And.intro hz hP
  exact Nat.mul_pos (by decide) hc

theorem field_parameter_count_positive_and_two_to_one {K L : Type*}
    [Field K] [Fintype K] [Field L] [Fintype L] [Algebra K L] [CharP L 2]
    (hcard : Fintype.card L = (Fintype.card K)^4)
    {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    (hm : p*q ∣ Fintype.card K+1) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ Fintype.card K+1 → r ∣ p*q)
    (hpodd : p ≠ 2) (hqodd : q ≠ 2) (h : K) (hh : h ≠ 0)
    (v : rootsOfUnity (Fintype.card K+1) L) (hv : groupSupport h v)
    (hvorder : orderOf v = Fintype.card K+1)
    (w : rootsOfUnity (Fintype.card K+1) L) (hw : groupSupport h w)
    (hwv : PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc w ≠
      PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc v)
    (hwvi : PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc w ≠
      -(PaperA.MultiplicativeSupport.groupCoordinates
      (finite_base_norm_group_card K L hcard) hm hc v)) :
    ∀ u : rootsOfUnity (Fintype.card K+1) L,
      let P := fun z : L => orderOf (z * (rootValue u) ^ (-2 : ℤ)) = Fintype.card K+1
      0 < (PaperA.ReciprocalTraceCounting.filteredSource
        (Fintype.card K) (algebraMap K L h) P).card ∧
      (PaperA.ReciprocalTraceCounting.filteredSource
        (Fintype.card K) (algebraMap K L h) P).card =
        2 * (filteredGroupSupport h P).card := by
  intro u
  obtain ⟨z, hz, horder⟩ := field_support_all_translates
    hcard hm hc hpr hpodd hqodd h v hv hvorder w hw hwv hwvi u
  constructor
  · apply parameter_count_positive_of_group_witness h hh _ z hz
    have hval := (rootValue_orderOf (z * u ^ (-2 : ℤ))).trans horder
    rwa [rootValue_mul_inv_sq] at hval
  · exact parameter_count_eq_two_mul_group_support_count h hh _

#print axioms roots_card_of_dvd
#print axioms plus_one_dvd_quartic_sub_one
#print axioms norm_group_card
#print axioms rootValue_injective
#print axioms rootValue_inv
#print axioms rootValue_orderOf
#print axioms groupSupport_inverse
#print axioms rootValue_mul_inv_sq
#print axioms finite_base_norm_group_card
#print axioms field_support_all_translates
#print axioms group_support_count_eq_field_support_count
#print axioms parameter_count_eq_two_mul_group_support_count
#print axioms parameter_count_positive_of_group_witness
#print axioms field_parameter_count_positive_and_two_to_one

end PaperA.NormOneSupportBridge
