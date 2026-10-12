# Model K v1 Unified Circuit Architecture

This file describes the **legacy Model K v1** circuit baseline, not the proposed Aethernox v2 64-bit logical-data specification.

Layers: Boolean gates -> half/full adders -> K2 two-bit adder -> 8-bit ripple adder/subtractor -> ALU -> registers/flags -> instruction decode/control -> byte-addressed legacy record memory.

## K2 equations

S0 = A0 XOR B0 XOR C0

C1 = (A0 AND B0) OR (C0 AND (A0 XOR B0))

S1 = A1 XOR B1 XOR C1

C2 = (A1 AND B1) OR (C1 AND (A1 XOR B1))

For C0=0, output bits are C2 S1 S0.

## Aethernox v2 relationship

Aethernox v2 proposes 64-bit logical values and 64-byte records. The existing 8-bit datapath can process those values using multi-byte routines; this is not a native 64-bit CPU. See `docs/64BIT_ARCHITECTURE_V2.md` and `asm/docs/64BIT_MIGRATION.md`.