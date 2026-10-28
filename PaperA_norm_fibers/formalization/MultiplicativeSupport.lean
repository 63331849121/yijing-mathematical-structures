import Mathlib.GroupTheory.SpecificGroups.Cyclic
import CyclicSupport

/-!+# Multiplicative cyclic groups and the inverse-support exponent model

The exponent equivalence is constructed from `IsCyclic G` and the actual
finite cardinality, rather than supplied as an unproved interface hypothesis.
Full order and the word `z * u^(-2)` are transported by this equivalence.
The final theorem transfers the two-odd-prime third-witness criterion to `G`.

No finite-field Frobenius, reciprocal-trace fibres, or fibre cardinalities are
formalized in this module.
-/

namespace PaperA.MultiplicativeSupport

variable {G : Type*} [Group G] [Fintype G] [IsCyclic G]

noncomputable def exponentEquiv {n : ℕ} (hcard : Fintype.card G = n) :
    G ≃* Multiplicative (ZMod n) := by
  have hn : Nat.card G = n := by
    simpa only [Nat.card_eq_fintype_card] using hcard
  exact hn ▸ (zmodCyclicMulEquiv (G := G) inferInstance).symm

noncomputable def exponent {n : ℕ} (hcard : Fintype.card G = n) (g : G) : ZMod n :=
  Multiplicative.toAdd (exponentEquiv hcard g)

noncomputable def element {n : ℕ} (hcard : Fintype.card G = n) (a : ZMod n) : G :=
  (exponentEquiv hcard).symm (Multiplicative.ofAdd a)

theorem exponent_element {n : ℕ} (hcard : Fintype.card G = n) (a : ZMod n) :
    exponent hcard (element hcard a) = a := by
  unfold exponent element
  rw [MulEquiv.apply_symm_apply]
  rfl

theorem element_exponent {n : ℕ} (hcard : Fintype.card G = n) (g : G) :
    element hcard (exponent hcard g) = g := by
  unfold element exponent
  exact MulEquiv.symm_apply_apply _ _

theorem exponent_injective {n : ℕ} (hcard : Fintype.card G = n) :
    Function.Injective (exponent hcard) := by
  intro x y h
  have h' := congrArg (element hcard) h
  simpa only [element_exponent] using h'

theorem exponent_surjective {n : ℕ} (hcard : Fintype.card G = n) :
    Function.Surjective (exponent hcard) := by
  intro a
  exact ⟨element hcard a, exponent_element hcard a⟩

theorem exponent_one {n : ℕ} (hcard : Fintype.card G = n) :
    exponent hcard (1 : G) = 0 := by
  unfold exponent
  rw [map_one]
  rfl

theorem exponent_mul {n : ℕ} (hcard : Fintype.card G = n) (g h : G) :
    exponent hcard (g*h) = exponent hcard g + exponent hcard h := by
  unfold exponent
  rw [map_mul]
  rfl

theorem exponent_inv {n : ℕ} (hcard : Fintype.card G = n) (g : G) :
    exponent hcard g⁻¹ = -(exponent hcard g) := by
  unfold exponent
  rw [map_inv]
  rfl

theorem exponent_zpow {n : ℕ} (hcard : Fintype.card G = n) (g : G) (k : ℤ) :
    exponent hcard (g^k) = k • exponent hcard g := by
  unfold exponent
  rw [map_zpow]
  exact toAdd_zpow _ _

theorem exponent_mul_inv_sq {n : ℕ} (hcard : Fintype.card G = n) (z u : G) :
    exponent hcard (z * u ^ (-2 : ℤ)) = exponent hcard z - 2 * exponent hcard u := by
  rw [exponent_mul, exponent_zpow, zsmul_eq_mul]
  simp only [Int.cast_neg, Int.cast_ofNat, neg_mul, sub_eq_add_neg]

theorem exponent_orderOf {n : ℕ} (hcard : Fintype.card G = n) (g : G) :
    addOrderOf (exponent hcard g) = orderOf g := by
  change orderOf (exponentEquiv hcard g) = orderOf g
  exact MulEquiv.orderOf_eq _ _

theorem full_order_iff_exponent_unit {n : ℕ} [NeZero n]
    (hcard : Fintype.card G = n) (g : G) :
    orderOf g = n ↔ IsUnit (exponent hcard g) := by
  rw [PaperA.CyclicSupport.isUnit_iff_full_addOrder, exponent_orderOf]

theorem element_neg {n : ℕ} (hcard : Fintype.card G = n) (a : ZMod n) :
    element hcard (-a) = (element hcard a)⁻¹ := by
  apply exponent_injective hcard
  rw [exponent_element, exponent_inv, exponent_element]

def exponentSupport {n : ℕ} (hcard : Fintype.card G = n)
    (S : G → Prop) (a : ZMod n) : Prop := S (element hcard a)

theorem exponentSupport_neg_closed {n : ℕ} (hcard : Fintype.card G = n)
    (S : G → Prop) (hS : ∀ g, S g → S g⁻¹) :
    ∀ a, exponentSupport hcard S a → exponentSupport hcard S (-a) := by
  intro a ha
  change S (element hcard (-a))
  rw [element_neg]
  exact hS _ ha

theorem exponentSupport_at_exponent {n : ℕ} (hcard : Fintype.card G = n)
    (S : G → Prop) (g : G) : exponentSupport hcard S (exponent hcard g) ↔ S g := by
  unfold exponentSupport
  rw [element_exponent]

theorem exists_full_order_iff_exponent {n : ℕ} [NeZero n]
    (hcard : Fintype.card G = n) (S : G → Prop) (u : G) :
    (∃ z, S z ∧ orderOf (z * u ^ (-2 : ℤ)) = n) ↔
      ∃ a : ZMod n, exponentSupport hcard S a ∧
        IsUnit (a - 2 * exponent hcard u) := by
  constructor
  · rintro ⟨z,hz,horder⟩
    refine ⟨exponent hcard z,(exponentSupport_at_exponent hcard S z).mpr hz,?_⟩
    have hunit := (full_order_iff_exponent_unit hcard (z*u^(-2 : ℤ))).mp horder
    rwa [exponent_mul_inv_sq] at hunit
  · rintro ⟨a,ha,hunit⟩
    refine ⟨element hcard a,ha,?_⟩
    apply (full_order_iff_exponent_unit hcard _).mpr
    rwa [exponent_mul_inv_sq, exponent_element]

noncomputable def groupCoordinates {n p q : ℕ} (hcard : Fintype.card G = n)
    (hm : p*q ∣ n) (hc : p.Coprime q) (g : G) : ZMod p × ZMod q :=
  PaperA.CyclicSupport.coordinates hm hc (exponent hcard g)

theorem groupCoordinates_inv {n p q : ℕ} (hcard : Fintype.card G = n)
    (hm : p*q ∣ n) (hc : p.Coprime q) (g : G) :
    groupCoordinates hcard hm hc g⁻¹ = -(groupCoordinates hcard hm hc g) := by
  unfold groupCoordinates
  rw [exponent_inv, map_neg]

theorem third_witness_all_translates {n p q : ℕ}
    [Fact p.Prime] [Fact q.Prime] (hcard : Fintype.card G = n)
    (hm : p*q ∣ n) (hc : p.Coprime q)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ n → r ∣ p*q)
    (hpodd : p ≠ 2) (hqodd : q ≠ 2)
    (S : G → Prop) (hS : ∀ z, S z → S z⁻¹)
    (v : G) (hv : S v) (hvorder : orderOf v = n)
    (w : G) (hw : S w)
    (hwv : groupCoordinates hcard hm hc w ≠ groupCoordinates hcard hm hc v)
    (hwvi : groupCoordinates hcard hm hc w ≠ -(groupCoordinates hcard hm hc v)) :
    ∀ u : G, ∃ z, S z ∧ orderOf (z * u ^ (-2 : ℤ)) = n := by
  letI : NeZero n := ⟨by
    rw [← hcard]
    exact Fintype.card_ne_zero⟩
  have hneg := exponentSupport_neg_closed hcard S hS
  have hv' := (exponentSupport_at_exponent hcard S v).mpr hv
  have hw' := (exponentSupport_at_exponent hcard S w).mpr hw
  have hvunit := (full_order_iff_exponent_unit hcard v).mp hvorder
  have hex := PaperA.CyclicSupport.third_witness_all_translates_unit hm hc hpr
    hpodd hqodd (exponentSupport hcard S) hneg
    (exponent hcard v) hv' hvunit (exponent hcard w) hw' hwv hwvi
  intro u
  apply (exists_full_order_iff_exponent hcard S u).mpr
  exact hex (exponent hcard u)

#print axioms exponentEquiv
#print axioms exponent
#print axioms element
#print axioms exponentSupport
#print axioms groupCoordinates
#print axioms exponent_element
#print axioms element_exponent
#print axioms exponent_injective
#print axioms exponent_surjective
#print axioms exponent_one
#print axioms exponent_mul
#print axioms exponent_inv
#print axioms exponent_zpow
#print axioms exponent_mul_inv_sq
#print axioms exponent_orderOf
#print axioms full_order_iff_exponent_unit
#print axioms element_neg
#print axioms exponentSupport_neg_closed
#print axioms exponentSupport_at_exponent
#print axioms exists_full_order_iff_exponent
#print axioms groupCoordinates_inv
#print axioms third_witness_all_translates

end PaperA.MultiplicativeSupport
