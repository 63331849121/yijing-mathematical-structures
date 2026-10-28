import InverseSupportGrid

/-!
Additional exact cover classifications used by the inverse-support argument.
These are constructive, coordinate-level theorems. The fixed-point property
of the involution is an explicit hypothesis; no cyclic-group or field claim
is hidden in this file. Counts and quotient-fiber sizes are not formalized.
-/

namespace PaperA.SupportCoverBranches

open PaperA.InverseSupportGrid

variable {A B : Type}

def CoverOne (S : A → Prop) (x : A) : Prop := ∀ z, S z → z = x

theorem empty_support_cover_one (x : A) : CoverOne (fun _ : A => False) x := by
  intro z hz
  exact False.elim hz

theorem inverse_closed_one_cover_iff
    (inv : A → A) (identity : A)
    (hfixed : ∀ a, inv a = a → a = identity)
    (S : A → Prop) (hS : ∀ z, S z → S (inv z))
    (hne : ∃ z, S z) (x : A) :
    CoverOne S x ↔ (∀ z, S z → z = identity) ∧ x = identity := by
  constructor
  · intro hx
    obtain ⟨z, hz⟩ := hne
    have hzx : z = x := hx z hz
    have hizx : inv z = x := hx (inv z) (hS z hz)
    have hzi : z = identity := hfixed z (hizx.trans hzx.symm)
    have hxi : x = identity := hzx.symm.trans hzi
    exact ⟨fun w hw => (hx w hw).trans hxi, hxi⟩
  · intro h z hz
    exact (h.1 z hz).trans h.2.symm

theorem inverse_closed_pair_cover_iff
    (ia : A → A) (ib : B → B)
    (hia : ∀ a, ia (ia a) = a) (hib : ∀ b, ib (ib b) = b)
    (S : A × B → Prop)
    (hS : ∀ z, S z → S (inversePoint ia ib z))
    (a : A) (b : B) (ha : a ≠ ia a) (hb : b ≠ ib b)
    (hv : S (a,b)) (x : A × B) :
    Cover S x ↔
      (∀ z, S z ↔ z = (a,b) ∨ z = (ia a,ib b)) ∧
      (x = (a,ib b) ∨ x = (ia a,b)) := by
  constructor
  · intro hx
    have hsub := covered_inverse_support_is_pair ia ib hia hib S hS a b ha hb hv x hx
    have hvi : S (ia a,ib b) := hS (a,b) hv
    have hpair : ∀ z, S z ↔ z = (a,b) ∨ z = (ia a,ib b) := by
      intro z
      constructor
      · exact hsub z
      · intro hz
        cases hz with
        | inl h => cases h; exact hv
        | inr h => cases h; exact hvi
    exact ⟨hpair, mixed_corners ia ib S a b ha hb hv hvi x hx⟩
  · intro h
    exact (inverse_pair_cover_iff ia ib S a b ha hb h.1 x).mpr h.2

theorem axis_support_cover_iff
    (S : A × B → Prop) (identity : A)
    (haxis : ∀ z, S z → z.1 = identity)
    (b c : B) (hbc : b ≠ c)
    (hb : S (identity,b)) (hc : S (identity,c))
    (x : A × B) : Cover S x ↔ x.1 = identity := by
  constructor
  · intro hx
    have h1 := hx (identity,b) hb
    have h2 := hx (identity,c) hc
    cases h1 with
    | inl h => exact h.symm
    | inr h =>
      cases h2 with
      | inl h' => exact h'.symm
      | inr h' => exact False.elim (hbc (h.trans h'.symm))
  · intro hx z hz
    exact Or.inl ((haxis z hz).trans hx.symm)

#print axioms empty_support_cover_one
#print axioms inverse_closed_one_cover_iff
#print axioms inverse_closed_pair_cover_iff
#print axioms axis_support_cover_iff

end PaperA.SupportCoverBranches
