# Model QK — Aethernox Paradox Core Reference Architecture

**Research snapshot:** 11 October 2026  
**Project name:** Model QK  
**Tagline:** *Two realms, one core.*

This repository is an educational experimental computer architecture. **Model K v1 (legacy)** is the legacy 8-bit reference design built from Boolean gates, a K2 two-bit adder, an 8-bit ALU, registers, control logic, assembly routines, and legacy fixed-size records. **Aethernox v2** is the proposed evolution toward 64-bit logical values and a modern, backend-neutral memory hierarchy.

## Version boundaries

- **Model K v1 (legacy):** 8-bit datapath, legacy 20-bit logical operations and existing 20-byte record schemas.
- **Aethernox v2:** proposed 64-bit logical data and 64-byte records, with explicit schema versioning.
- **Native 64-bit CPU:** optional future hardware design; not implied by 64-bit logical values on an 8-bit CPU.
- **Memory:** SRAM/FPGA block RAM for initial prototype; DRAM where platform-supported; NVMe/NAND for persistent bulk storage; optional MRAM study; ferrite magnetic-core memory as a separate historical laboratory experiment.
- **Quantum:** the existing `quantum/` subsystem is intentionally unchanged by the 2026 memory/record refresh. It remains a separate QISA/QASM simulator/backend interface.

## Current documents

- [2026 research refresh](docs/2026_RESEARCH_REFRESH.md)
- [Aethernox v2 64-bit architecture](docs/64BIT_ARCHITECTURE_V2.md)
- [2026 hardware and memory plan](docs/2026_HARDWARE_AND_MEMORY_PLAN.md)
- [Aethernox v2 record format](database/RECORD_FORMAT_V2.md)
- [64-bit operations on the 8-bit CPU](asm/docs/64BIT_MIGRATION.md)
- [Legacy Model K architecture](docs/00-ARCHITECTURE.md)
- [Legacy Model K record layout](docs/03-20-BYTE-RECORD.md)

## Build targets

Hardware/RTL test:
```sh
make test
```

Portable native reference executable:
```sh
make compile
make compile-test
```

The native executable is a compiled reference implementation of Model K logical semantics. It is not the physical CPU machine-code image. The RTL and assembly specifications remain reference material; v2 functionality is not considered implemented until code and tests are added.

## Source tree

- `rtl/` — SystemVerilog hardware model
- `asm/` — conventional assembly/reference algorithms
- `compile/` — portable C11 compiled reference
- `database/` — legacy and v2 record/data formats
- `quantum/` — QISA, circuits, simulator, and classical/quantum interface (unchanged in this refresh)
- `update/` — versioned update and patch design
- `shell/` — Model K DOS-style shell
- `seed/` — deterministic seed subsystem
- `docs/` — architecture, mathematics, research, and hardware plans
- `tests/` — verification material

## Legacy v1 arithmetic and records

`0 <= x <= 2^20 - 1 = 1,048,575`

`0xFFFFF + 1 = 0x00000` under 20-bit modular arithmetic.

Legacy physical records are 20 bytes. They are not the same thing as 20-bit logical values.

## v2 logical values

`0 <= x <= 2^64 - 1`

The v2 proposal uses 64-bit logical values and 64-byte records. Legacy v1 records must be parsed with their declared schema and migrated explicitly; never reinterpret their bytes in place.

## Update and patch workflow

`CHECK -> VERIFY -> STAGE -> APPLY -> TEST -> COMMIT`

On failure: `ROLLBACK -> VERIFY`.

See `update/` for patch manifests, SHA-256 integrity rules, dependency resolution, rollback metadata, and update commands.

## Implementation status

The 2026 research and v2 specifications are design documents. This commit does not claim that every legacy ASM routine, RTL module, C implementation, or test has been converted to v2. Implementation status must be tracked per module and confirmed by builds and tests.


## Project rename

The current project name is **Model QK**. Legacy `model_k`, `mk_`, and `MK` source identifiers remain compatibility namespaces until an explicit ABI/RTL migration is completed. See `docs/MODEL_QK_RENAME.md` and `docs/PROJECT_IDENTITY.md`.
