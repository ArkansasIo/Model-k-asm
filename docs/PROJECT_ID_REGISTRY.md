# Model QK Folder / Program / File Identity Registry

**Registry ID:** QK-IDREG-2026-001  
**Project:** Model QK — Aethernox Paradox Core  
**Registry version:** 2.0  
**Date:** 2026-10-11

## Naming policy

Every tracked subsystem receives a stable **Folder ID**, subsystem **Program ID**, and version. Individual source files use the folder/program ID plus a four-digit sequence when a permanent file identity is required.

Legacy `Model K`, `MK`, and `model_k_*` identifiers remain compatibility aliases. They are not silently renamed because they can be part of existing source paths, ABI names, RTL module names, database schemas, or tests.

## Folder registry

| ID | Path | Name | Program ID |
|---|---|---|---|
| FOLDER-000 | `/` | Model QK repository root | `QK-REPO-0001` |
| FOLDER-001 | `/asm` | Classical assembly | `QK-ASM-0001` |
| FOLDER-002 | `/rtl` | Classical RTL | `QK-RTL-0001` |
| FOLDER-003 | `/tb` | RTL testbench | `QK-TB-0001` |
| FOLDER-004 | `/compile` | Native reference build | `QK-CMP-0001` |
| FOLDER-005 | `/database` | Data and record formats | `QK-DB-0001` |
| FOLDER-006 | `/docs` | Architecture and research documentation | `QK-DOC-0001` |
| FOLDER-007 | `/config` | Runtime configuration | `QK-CFG-0001` |
| FOLDER-008 | `/seed` | Deterministic seed subsystem | `QK-SED-0001` |
| FOLDER-009 | `/shell` | Command shell | `QK-SHL-0001` |
| FOLDER-010 | `/update` | Update and patch subsystem | `QK-UPD-0001` |
| FOLDER-011 | `/quantum` | Quantum computing research subsystem | `QK-QNT-0001` |
| FOLDER-012 | `/quantum/apps` | Quantum applications | `QK-QAPP-0001` |
| FOLDER-013 | `/quantum/asm` | Quantum assembly | `QK-QASM-0001` |
| FOLDER-014 | `/quantum/backend` | Quantum backend contract | `QK-QBE-0001` |
| FOLDER-015 | `/quantum/circuits` | Quantum circuits | `QK-QCIR-0001` |
| FOLDER-016 | `/quantum/compiler` | Quantum compiler | `QK-QCMP-0001` |
| FOLDER-017 | `/quantum/control` | Quantum control abstraction | `QK-QCTL-0001` |
| FOLDER-018 | `/quantum/error_correction` | Quantum error correction | `QK-QEC-0001` |
| FOLDER-019 | `/quantum/hardware` | Quantum hardware abstraction | `QK-QHW-0001` |
| FOLDER-020 | `/quantum/hardware/virtual` | Virtual quantum hardware | `QK-QVHW-0001` |
| FOLDER-021 | `/quantum/isa` | Quantum ISA | `QK-QISA-0001` |
| FOLDER-022 | `/quantum/math` | Quantum mathematics | `QK-QMAT-0001` |
| FOLDER-023 | `/quantum/plugins` | Physical-platform plugins | `QK-QPLG-0001` |
| FOLDER-024 | `/quantum/scheduler` | Quantum scheduler | `QK-QSCH-0001` |
| FOLDER-025 | `/quantum/sim` | Quantum simulators | `QK-QSIM-0001` |
| FOLDER-026 | `/quantum/tests` | Quantum verification | `QK-QTST-0001` |

## File identity

Format: `<PROGRAM-ID>-FILE-####`.

Examples:
- `QK-QSIM-0001-FILE-0001` — state-vector simulator
- `QK-QVHW-0001-FILE-0001` — virtual QPU
- `QK-QAPP-0001-FILE-0001` — procedural generator
- `QK-ASM-0001-FILE-0001` — classical assembly runtime

## Version identity

Format: `QK.<major>.<minor>.<patch>`.

- Major: incompatible architecture/schema change
- Minor: compatible subsystem feature
- Patch: bug fix/documentation/test change

## Numeric identity

Repository-wide numeric namespaces:
- 0000–0999: architecture and root metadata
- 1000–1999: classical CPU/ASM/RTL
- 2000–2999: memory/database/storage
- 3000–3999: operating-system/shell/update
- 4000–4999: quantum software
- 5000–5999: virtual hardware and simulation
- 6000–6999: physical hardware adapters
- 7000–7999: tests/verification
- 8000–8999: research/documentation
- 9000–9999: reserved/extensions

## Rule

IDs identify artifacts; names identify human-facing concepts; numbers identify stable registry slots. Changing a display name must not change an existing ID.
