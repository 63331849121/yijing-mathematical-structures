import Lake
open Lake DSL

package paperA

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "fabf563a7c95a166b8d7b6efca11c8b4dc9d911f"

@[default_target]
lean_lib PaperAInterfaces where
  roots := #[`InverseSupportGrid, `SupportCoverBranches,
             `CyclicSupport, `ReciprocalTraceSupport, `MultiplicativeSupport,
             `ReciprocalTraceCounting, `NormOneSupportBridge,
             `RelativeTraceTransfer, `NamedNormTraceTransfer]
