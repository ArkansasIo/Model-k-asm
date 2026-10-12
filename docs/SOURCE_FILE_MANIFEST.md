# Model QK Source File Manifest

**Registry:** QK-IDREG-2026-001  
**Version:** QK.2.0.0

## Classical executable/reference sources

| File ID | Path | Purpose |
|---|---|---|
| QK-ASM-0001-FILE-0001 | asm/model_k.asm | Legacy assembly entry point |
| QK-ASM-0001-FILE-0002 | asm/model_k_runtime.asm | Runtime primitives |
| QK-ASM-0001-FILE-0003 | asm/model_k_math.asm | Legacy arithmetic |
| QK-RTL-0001-FILE-0001 | rtl/model_k.sv | Legacy RTL top |
| QK-CMP-0001-FILE-0001 | compile/src/model_k.c | Legacy C reference |
| QK-CMP-0001-FILE-0002 | compile/src/model_qk.c | 64-bit QK C reference |
| QK-CMP-0001-FILE-0003 | compile/src/qk.c | QK CLI reference |

## Quantum executable/reference sources

| File ID | Path | Purpose |
|---|---|---|
| QK-QAPP-0001-FILE-0001 | quantum/apps/procedural_generator.py | Procedural circuit generator |
| QK-QAPP-0001-FILE-0002 | quantum/apps/virtual_hardware.py | Virtual QPU application |
| QK-QBE-0001-FILE-0002 | quantum/backend/model_qk_simulator_backend.py | State-vector backend |
| QK-QCMP-0001-FILE-0001 | quantum/compiler/model_qk_compiler.py | Operation validation/lowering |
| QK-QSCH-0001-FILE-0001 | quantum/scheduler/model_qk_scheduler.py | Quantum job scheduler |
| QK-QVHW-0001-FILE-0001 | quantum/sim/model_qk_virtual_hardware.py | Virtual hardware model |
| QK-QSIM-0001-FILE-0001 | quantum/sim/aethernox_statevector.py | State-vector simulator |

## Rule

Documentation files describe contracts; executable files implement those contracts. Legacy Model K files remain source-compatible references and are not deleted during the Model QK migration.
