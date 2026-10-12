import Mathlib

/-!
Function-level triality for complete mappings of an additive group of exponent two.
This file covers Lemmas 4.1 and 4.2, not the orbit counts or the PTE theorem.
-/

namespace CompleteMappingTriality

structure CompleteMapping (V : Type*) [AddCommGroup V] where
  perm : V ≃ V
  sumPerm : V ≃ V
  sum_eq : ∀ x, sumPerm x = x + perm x

variable {V : Type*} [AddCommGroup V]

def rotate (h2 : ∀ x : V, x + x = 0) (c : CompleteMapping V) : CompleteMapping V where
  perm := c.sumPerm.symm
  sumPerm := c.sumPerm.symm.trans c.perm
  sum_eq := by
    intro x
    let y := c.sumPerm.symm x
    have hx : y + c.perm y = x := by
      rw [← c.sum_eq]
      exact c.sumPerm.apply_symm_apply x
    change c.perm y = x + y
    calc
      c.perm y = (y + c.perm y) + y := by
        symm
        calc
          (y + c.perm y) + y = (y + y) + c.perm y := by abel
          _ = c.perm y := by rw [h2, zero_add]
      _ = x + y := by rw [hx]

theorem rotate_twice_apply (h2 : ∀ x : V, x + x = 0)
    (c : CompleteMapping V) (x : V) :
    (rotate h2 (rotate h2 c)).perm x = x + c.perm.symm x := by
  change c.sumPerm (c.perm.symm x) = x + c.perm.symm x
  rw [c.sum_eq]
  simp [add_comm]

theorem rotate_three (h2 : ∀ x : V, x + x = 0) (c : CompleteMapping V) :
    (rotate h2 (rotate h2 (rotate h2 c))).perm = c.perm := by
  have hs : (rotate h2 (rotate h2 c)).sumPerm = c.perm.symm := by
    apply Equiv.ext
    intro x
    change c.sumPerm.symm (c.sumPerm (c.perm.symm x)) = c.perm.symm x
    exact c.sumPerm.symm_apply_apply _
  change (rotate h2 (rotate h2 c)).sumPerm.symm = c.perm
  rw [hs]
  exact c.perm.symm_symm

theorem unique_fixed (h2 : ∀ x : V, x + x = 0)
    (c : CompleteMapping V) (x : V) :
    c.perm x = x ↔ x = c.sumPerm.symm 0 := by
  constructor
  · intro hx
    have hs : c.sumPerm x = 0 := by rw [c.sum_eq, hx, h2]
    exact (c.sumPerm.eq_symm_apply).2 hs
  · intro hx
    have hs : c.sumPerm x = 0 := by rw [hx]; exact c.sumPerm.apply_symm_apply _
    have hsum : x + c.perm x = x + x := by rw [← c.sum_eq, hs, h2]
    exact add_left_cancel hsum

end CompleteMappingTriality
