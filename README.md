# Model K — 8-bit Assembly, RTL, Core Memory, and Reference Build

Model K is an educational 8-bit computer reference design built from Boolean gates,
a K2 two-bit adder, an 8-bit ALU, registers, a compact CPU, byte-addressed
20-byte records, magnetic-core memory abstractions, and a quantum QISA boundary.

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

The native executable is a **compiled reference implementation** of the Model K
logical semantics. It is not the physical CPU machine-code image. The SystemVerilog
RTL and assembly specifications remain authoritative for hardware implementation.

## Source tree

- `rtl/` — SystemVerilog hardware model
- `asm/` — assembly/reference algorithms
- `compile/` — portable C11 compiled reference
- `database/` — record/database formats
- `quantum/` — QISA, circuits, simulator, and classical/quantum interface
- `update/` — versioned update and patch system
- `shell/` — Model K DOS-style shell
- `seed/` — deterministic seed subsystem
- `docs/` — architecture and mathematics
- `tests/` — verification material

## 20-bit arithmetic

`0 <= x <= 2^20 - 1 = 1,048,575`

Therefore:
`0xFFFFF + 1 = 0x00000`

## 20-byte records

`20 bytes = 160 bits`

These physical records are distinct from the 20-bit logical value type.

## Update and patch workflow

`CHECK -> VERIFY -> STAGE -> APPLY -> TEST -> COMMIT`

On failure:
`ROLLBACK -> VERIFY`

See `update/` for patch manifests, SHA-256 integrity rules, dependency
resolution, rollback metadata, and update commands.
