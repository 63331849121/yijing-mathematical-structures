import Init

/-!
The two-coordinate combinatorial core of the inverse-support reduction.

This file has no mathlib dependency. Involutions and inverse closure are
explicit hypotheses. It does not formalize cyclic-group CRT, finite-field
Frobenius, the order indicators, certificate arithmetic, or Theorem 5.4.
-/

namespace PaperA.InverseSupportGrid

variable {A B : Type}

def inversePoint (ia : A → A) (ib : B → B) (z : A × B) : A × B :=
  (ia z.1, ib z.2)

def Cover (S : A × B → Prop) (x : A × B) : Prop :=
  ∀ z, S z → z.1 = x.1 ∨ z.2 = x.2

theorem cover_inverse
    (ia : A → A) (ib : B → B)
    (hia : ∀ a, ia (ia a) = a) (hib : ∀ b, ib (ib b) = b)
    (S : A × B → Prop)
    (hS : ∀ z, S z → S (inversePoint ia ib z))
    (x : A × B) (hx : Cover S x) :
    Cover S (inversePoint ia ib x) := by
  intro z hz
  have h := hx (inversePoint ia ib z) (hS z hz)
  cases h with
  | inl ha =>
      apply Or.inl
      have eqn := congrArg ia ha
      change ia (ia z.1) = ia x.1 at eqn
      rw [hia z.1] at eqn
      exact eqn
  | inr hb =>
      apply Or.inr
      have eqn := congrArg ib hb
      change ib (ib z.2) = ib x.2 at eqn
      rw [hib z.2] at eqn
      exact eqn

theorem mixed_corners
    (ia : A → A) (ib : B → B)
    (S : A × B → Prop) (a : A) (b : B)
    (ha : a ≠ ia a) (hb : b ≠ ib b)
    (hv : S (a,b)) (hvi : S (ia a,ib b))
    (x : A × B) (hx : Cover S x) :
    x = (a,ib b) ∨ x = (ia a,b) := by
  have h1 := hx (a,b) hv
  have h2 := hx (ia a,ib b) hvi
  cases h1 with
  | inl hax =>
      cases h2 with
      | inl hiax => exact False.elim (ha (hax.trans hiax.symm))
      | inr hibx =>
          exact Or.inl (Prod.ext hax.symm hibx.symm)
  | inr hbx =>
      cases h2 with
      | inl hiax =>
          exact Or.inr (Prod.ext hiax.symm hbx.symm)
      | inr hibx => exact False.elim (hb (hbx.trans hibx.symm))

theorem two_crosses_intersect_in_inverse_pair
    (ia : A → A) (ib : B → B)
    (S : A × B → Prop) (a : A) (b : B)
    (ha : a ≠ ia a) (hb : b ≠ ib b)
    (h1 : Cover S (a,ib b)) (h2 : Cover S (ia a,b)) :
    ∀ z, S z → z = (a,b) ∨ z = (ia a,ib b) := by
  intro z hz
  have hc1 := h1 z hz
  have hc2 := h2 z hz
  cases hc1 with
  | inl hza =>
      cases hc2 with
      | inl hzia => exact False.elim (ha (hza.symm.trans hzia))
      | inr hzb => exact Or.inl (Prod.ext hza hzb)
  | inr hzib =>
      cases hc2 with
      | inl hzia => exact Or.inr (Prod.ext hzia hzib)
      | inr hzb => exact False.elim (hb (hzb.symm.trans hzib))

theorem covered_inverse_support_is_pair
    (ia : A → A) (ib : B → B)
    (hia : ∀ a, ia (ia a) = a) (hib : ∀ b, ib (ib b) = b)
    (S : A × B → Prop)
    (hS : ∀ z, S z → S (inversePoint ia ib z))
    (a : A) (b : B) (ha : a ≠ ia a) (hb : b ≠ ib b)
    (hv : S (a,b)) (x : A × B) (hx : Cover S x) :
    ∀ z, S z → z = (a,b) ∨ z = (ia a,ib b) := by
  have hvi := hS (a,b) hv
  have hi := cover_inverse ia ib hia hib S hS x hx
  have hc := mixed_corners ia ib S a b ha hb hv hvi x hx
  cases hc with
  | inl hcorner =>
      subst x
      have hi' : Cover S (ia a,b) := by
        simpa [inversePoint,hib] using hi
      exact two_crosses_intersect_in_inverse_pair ia ib S a b ha hb hx hi'
  | inr hcorner =>
      subst x
      have hi' : Cover S (a,ib b) := by
        simpa [inversePoint,hia] using hi
      exact two_crosses_intersect_in_inverse_pair ia ib S a b ha hb hi' hx

theorem third_point_excludes_cover
    (ia : A → A) (ib : B → B)
    (hia : ∀ a, ia (ia a) = a) (hib : ∀ b, ib (ib b) = b)
    (S : A × B → Prop)
    (hS : ∀ z, S z → S (inversePoint ia ib z))
    (a : A) (b : B) (ha : a ≠ ia a) (hb : b ≠ ib b)
    (hv : S (a,b)) (w : A × B) (hw : S w)
    (hwv : w ≠ (a,b)) (hwvi : w ≠ (ia a,ib b)) :
    ∀ x, ¬ Cover S x := by
  intro x hx
  have hp := covered_inverse_support_is_pair ia ib hia hib S hS a b ha hb hv x hx w hw
  cases hp with
  | inl h => exact hwv h
  | inr h => exact hwvi h

theorem inverse_pair_cover_iff
    (ia : A → A) (ib : B → B)
    (S : A × B → Prop) (a : A) (b : B)
    (ha : a ≠ ia a) (hb : b ≠ ib b)
    (hpair : ∀ z, S z ↔ z = (a,b) ∨ z = (ia a,ib b))
    (x : A × B) :
    Cover S x ↔ x = (a,ib b) ∨ x = (ia a,b) := by
  constructor
  · intro hx
    have hv : S (a,b) := (hpair (a,b)).mpr (Or.inl rfl)
    have hvi : S (ia a,ib b) := (hpair (ia a,ib b)).mpr (Or.inr rfl)
    exact mixed_corners ia ib S a b ha hb hv hvi x hx
  · intro hc z hz
    have hp := (hpair z).mp hz
    cases hc with
    | inl hcorner =>
        subst x
        cases hp with
        | inl hv => cases hv; exact Or.inl rfl
        | inr hvi => cases hvi; exact Or.inr rfl
    | inr hcorner =>
        subst x
        cases hp with
        | inl hv => cases hv; exact Or.inr rfl
        | inr hvi => cases hvi; exact Or.inl rfl

#print axioms cover_inverse
#print axioms mixed_corners
#print axioms two_crosses_intersect_in_inverse_pair
#print axioms covered_inverse_support_is_pair
#print axioms third_point_excludes_cover
#print axioms inverse_pair_cover_iff

end PaperA.InverseSupportGrid
