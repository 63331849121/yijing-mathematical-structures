import Mathlib

/-!
# Conditional formalization of the even-`q` Cohen input

This file does not prove Cohen (2003).  It isolates the exact external
even-`q` hypothesis needed by the paper and formalizes the order-theoretic
part of the tau-collapse that follows from it.
-/

namespace CohenEvenConditional

/-- `A k = 2^k - 1`. -/
def A (k : ℕ) : ℕ := 2 ^ k - 1

/-- `B k = 2^k + 1`. -/
def B (k : ℕ) : ℕ := 2 ^ k + 1

/-- `M k = (2^k - 1)(2^k + 1) = 2^(2k) - 1`. -/
def M (k : ℕ) : ℕ := A k * B k


lemma one_add_pow_sub_one_of_pow_eq_inv {L : Type*} [Field L] [CharP L 2]
    {k : ℕ} (_hk : 1 ≤ k) {γ : L}
    (hγpow : γ ^ (2 ^ k) = γ⁻¹) (hγne : γ ≠ 1) (hγne0 : γ ≠ 0) :
    (1 + γ) ^ (2 ^ k - 1) = γ⁻¹ := by
  have htwo : 1 ≤ 2 ^ k := by
    have hp : 0 < 2 ^ k := pow_pos (by norm_num) k
    omega
  have hsub : 2 ^ k - 1 + 1 = 2 ^ k := Nat.sub_add_cancel htwo
  have hpow : (1 + γ) ^ (2 ^ k) = 1 + γ⁻¹ := by
    have h := add_pow_char_pow (R := L) (x := 1) (y := γ) (p := 2) (n := k)
    simpa [hγpow] using h
  have hmul : (1 + γ) ^ (2 ^ k - 1) * (1 + γ) = 1 + γ⁻¹ := by
    rw [← pow_succ, hsub, hpow]
  have hnegone : (-1 : L) = 1 := by
    apply (neg_one_eq_one_iff).2
    exact ringChar.eq (R := L) 2
  have honeadd : 1 + γ ≠ 0 := by
    intro hzero
    have hγeq : γ = 1 := by
      have hneg : γ = -1 := eq_neg_of_add_eq_zero_right hzero
      simp [hneg, hnegone]
    exact hγne hγeq
  let X : L := (1 + γ) ^ (2 ^ k - 1)
  have hX : X * γ = 1 := by
    have hcalc : (X * γ) * (1 + γ) = (1 : L) * (1 + γ) := by
      calc
        (X * γ) * (1 + γ) = X * (1 + γ) * γ := by ring
        _ = (1 + γ⁻¹) * γ := by rw [hmul]
        _ = 1 + γ := by field_simp [hγne0]; ring
        _ = (1 : L) * (1 + γ) := by ring
    exact mul_right_cancel₀ honeadd hcalc
  exact eq_inv_of_mul_eq_one_left hX

lemma one_add_pow_add_one_of_pow_eq_inv {L : Type*} [Field L] [CharP L 2]
    {k : ℕ} {γ : L} (hγpow : γ ^ (2 ^ k) = γ⁻¹) (hγne0 : γ ≠ 0) :
    (1 + γ) ^ (2 ^ k + 1) = γ + γ⁻¹ := by
  have hpow : (1 + γ) ^ (2 ^ k) = 1 + γ⁻¹ := by
    have h := add_pow_char_pow (R := L) (x := 1) (y := γ) (p := 2) (n := k)
    simpa [hγpow] using h
  rw [pow_succ, hpow]
  ring_nf
  rw [mul_inv_cancel₀ hγne0]
  have h11 : (1 : L) + 1 = 0 := by
    norm_num
    exact CharP.cast_eq_zero L 2
  calc
    1 + γ + 1 + γ⁻¹ = (1 + 1) + γ + γ⁻¹ := by abel
    _ = 0 + γ + γ⁻¹ := by rw [h11]
    _ = γ + γ⁻¹ := by simp

lemma div_one_add_pow_sub_one_of_pow_eq_inv {L : Type*} [Field L] [CharP L 2]
    {k : ℕ} (hk : 1 ≤ k) {γ : L}
    (hγpow : γ ^ (2 ^ k) = γ⁻¹) (hγne : γ ≠ 1) (hγne0 : γ ≠ 0) :
    (γ / (1 + γ)) ^ (2 ^ k - 1) = γ⁻¹ := by
  have htwo : 1 ≤ 2 ^ k := by
    have hp : 0 < 2 ^ k := pow_pos (by norm_num) k
    omega
  have hsub : 2 ^ k - 1 + 1 = 2 ^ k := Nat.sub_add_cancel htwo
  have hdelta := one_add_pow_sub_one_of_pow_eq_inv (L := L) (k := k) hk hγpow hγne hγne0
  rw [div_eq_mul_inv, mul_pow, inv_pow, hdelta]
  rw [inv_inv]
  rw [← pow_succ, hsub, hγpow]

lemma div_one_add_pow_add_one_of_pow_eq_inv {L : Type*} [Field L] [CharP L 2]
    {k : ℕ} {γ : L} (hγpow : γ ^ (2 ^ k) = γ⁻¹) (hγne0 : γ ≠ 0) :
    (γ / (1 + γ)) ^ (2 ^ k + 1) = (γ + γ⁻¹)⁻¹ := by
  have hγpowB : γ ^ (2 ^ k + 1) = 1 := by
    rw [pow_succ, hγpow]
    field_simp [hγne0]
  have hdelta := one_add_pow_add_one_of_pow_eq_inv (L := L) (k := k) hγpow hγne0
  rw [div_eq_mul_inv, mul_pow, hγpowB]
  rw [inv_pow]
  rw [hdelta]
  simp

/-- In a field, inversion preserves order for nonzero elements. -/
lemma orderOf_inv_of_ne_zero {L : Type*} [Field L] {a : L} (ha : a ≠ 0) :
    orderOf a⁻¹ = orderOf a := by
  let u : Lˣ := Units.mk0 a ha
  change orderOf ((u⁻¹ : Lˣ) : L) = orderOf (u : L)
  calc
    orderOf ((u⁻¹ : Lˣ) : L) = orderOf (u⁻¹) :=
      orderOf_injective (Units.coeHom L) Units.val_injective (u⁻¹)
    _ = orderOf u := orderOf_inv u
    _ = orderOf ((u : Lˣ) : L) :=
      (orderOf_injective (Units.coeHom L) Units.val_injective u).symm

/-- From `ord γ = 2^k+1` derive the Frobenius power relation used by the
tau-collapse. -/
lemma pow_two_pow_eq_inv_of_order {L : Type*} [Field L] [CharP L 2]
    {k : ℕ} {γ : L} (hγ : orderOf γ = 2 ^ k + 1) :
    γ ^ (2 ^ k) = γ⁻¹ := by
  have h : γ ^ (2 ^ k + 1) = 1 := by
    simpa [hγ] using pow_orderOf_eq_one γ
  rw [pow_succ] at h
  exact eq_inv_of_mul_eq_one_left h

/-- The four field-level Frobenius identities used by the tau-collapse. -/
theorem frobenius_identities {L : Type*} [Field L] [CharP L 2]
    {k : ℕ} (hk : 1 ≤ k) {γ : L}
    (hγpow : γ ^ (2 ^ k) = γ⁻¹) (hγne : γ ≠ 1) (hγne0 : γ ≠ 0) :
    (1 + γ) ^ (2 ^ k - 1) = γ⁻¹ ∧
    (1 + γ) ^ (2 ^ k + 1) = γ + γ⁻¹ ∧
    (γ / (1 + γ)) ^ (2 ^ k - 1) = γ⁻¹ ∧
    (γ / (1 + γ)) ^ (2 ^ k + 1) = (γ + γ⁻¹)⁻¹ := by
  refine ⟨one_add_pow_sub_one_of_pow_eq_inv (L := L) (k := k) hk hγpow hγne hγne0, ?_⟩
  have hδB := one_add_pow_add_one_of_pow_eq_inv (L := L) (k := k) hγpow hγne0
  refine ⟨hδB, ?_⟩
  refine ⟨div_one_add_pow_sub_one_of_pow_eq_inv (L := L) (k := k) hk hγpow hγne hγne0, ?_⟩
  exact div_one_add_pow_add_one_of_pow_eq_inv (L := L) (k := k) hγpow hγne0

/--
The pure order-theoretic core: if `x^A = y`, `x^B = z`, the orders of
`y` and `z` are coprime `B` and `A`, then `x` has order `A*B`.
-/
lemma orderOf_eq_mul_of_pow_eq {G : Type*} [Monoid G]
    {x y z : G} {A B : ℕ} (hcop : Nat.Coprime A B)
    (hxA : x ^ A = y) (hxB : x ^ B = z)
    (hy : orderOf y = B) (hz : orderOf z = A) :
    orderOf x = A * B := by
  have hBdvd : B ∣ orderOf x := by
    rw [← hy, ← hxA]
    exact orderOf_pow_dvd A
  have hAdvd : A ∣ orderOf x := by
    rw [← hz, ← hxB]
    exact orderOf_pow_dvd B
  have hABdvd : A * B ∣ orderOf x :=
    hcop.mul_dvd_of_dvd_of_dvd hAdvd hBdvd
  have hxpow : x ^ (A * B) = 1 := by
    rw [pow_mul, hxA, ← hy, pow_orderOf_eq_one]
  have hxdvd : orderOf x ∣ A * B := orderOf_dvd_of_pow_eq_one hxpow
  exact Nat.dvd_antisymm hxdvd hABdvd

/-- Field-level tau-collapse: the four Frobenius identities and the stated
orders imply the two target orders directly, without passing through units. -/
theorem tau_collapse_orders_field {L : Type*} [Field L] [CharP L 2]
    {k : ℕ} (hk : 1 ≤ k) {γ : L}
    (hγpow : γ ^ (2 ^ k) = γ⁻¹) (hγne : γ ≠ 1) (hγne0 : γ ≠ 0)
    (hγinv_order : orderOf γ⁻¹ = B k)
    (hτ_order : orderOf (γ + γ⁻¹) = A k)
    (hτinv_order : orderOf (γ + γ⁻¹)⁻¹ = A k)
    (hcop : Nat.Coprime (A k) (B k)) :
    orderOf (1 + γ) = M k ∧ orderOf (γ / (1 + γ)) = M k := by
  have hident := frobenius_identities (L := L) (k := k) hk hγpow hγne hγne0
  constructor
  · simpa [M, A, B] using
      (orderOf_eq_mul_of_pow_eq (G := L)
        (x := 1 + γ) (y := γ⁻¹) (z := γ + γ⁻¹)
        (A := A k) (B := B k) hcop hident.1 hident.2.1
        hγinv_order hτ_order)
  · simpa [M, A, B] using
      (orderOf_eq_mul_of_pow_eq (G := L)
        (x := γ / (1 + γ)) (y := γ⁻¹) (z := (γ + γ⁻¹)⁻¹)
        (A := A k) (B := B k) hcop hident.2.2.1 hident.2.2.2
        hγinv_order hτinv_order)

/--
The exact algebraic data produced by the even-`q` branch of Cohen 1.5,
after moving to the unit group of the quadratic extension.

The field-specific Frobenius identities are represented by the four power
equalities.  A later file can construct these from `γ^(2^k) = γ⁻¹`.
-/
structure TauCollapseData (G : Type*) [Group G] (k : ℕ) where
  hcop : Nat.Coprime (A k) (B k)
  gamma : G
  delta : G
  u : G
  tau : G
  gamma_order : orderOf gamma = B k
  tau_order : orderOf tau = A k
  delta_pow_A : delta ^ A k = gamma⁻¹
  delta_pow_B : delta ^ B k = tau
  u_pow_A : u ^ A k = gamma⁻¹
  u_pow_B : u ^ B k = tau⁻¹

/--
Abstract tau-collapse: under the displayed Frobenius data, `δ = 1+γ`
and `u = γ/(1+γ)` both have order `M = A*B`.
-/
theorem tau_collapse_orders {G : Type*} [Group G] {k : ℕ}
    (D : TauCollapseData G k) :
    orderOf D.delta = M k ∧ orderOf D.u = M k := by
  constructor
  · simpa [M, A, B] using
      (orderOf_eq_mul_of_pow_eq (G := G)
        (x := D.delta) (y := D.gamma⁻¹) (z := D.tau)
        (A := A k) (B := B k) D.hcop
        D.delta_pow_A D.delta_pow_B
        (by rw [orderOf_inv, D.gamma_order])
        D.tau_order)
  · simpa [M, A, B] using
      (orderOf_eq_mul_of_pow_eq (G := G)
        (x := D.u) (y := D.gamma⁻¹) (z := D.tau⁻¹)
        (A := A k) (B := B k) D.hcop
        D.u_pow_A D.u_pow_B
        (by rw [orderOf_inv, D.gamma_order])
        (by rw [orderOf_inv, D.tau_order]))

/--
Exact external even-`q` Cohen interface.  This is a statement, not an axiom or
a proof.  The paper uses only this consequence of Cohen (2003), Theorem 1.5.
-/
structure CohenEvenData (k : ℕ) where
  F : Type
  [fieldF : Field F]
  [charF : CharP F 2]
  [fintypeF : Fintype F]
  cardF : Fintype.card F = 2 ^ k
  L : Type
  [fieldL : Field L]
  [charL : CharP L 2]
  [algebraFL : Algebra F L]
  [finiteDimensionalFL : FiniteDimensional F L]
  gamma : L
  tau : F
  gamma_order : orderOf gamma = B k
  tau_order : orderOf tau = A k
  tau_spec : algebraMap F L tau = gamma + gamma⁻¹

end CohenEvenConditional
