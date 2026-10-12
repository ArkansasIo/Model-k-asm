# Model K Unified Circuit Architecture

Layers: Boolean gates -> half/full adders -> K2 two-bit adder -> 8-bit ripple adder/subtractor -> ALU -> registers/flags -> instruction decode/control -> byte-addressed record memory.

## K2 equations

S0 = A0 XOR B0 XOR C0

C1 = (A0 AND B0) OR (C0 AND (A0 XOR B0))

S1 = A1 XOR B1 XOR C1

C2 = (A1 AND B1) OR (C1 AND (A1 XOR B1))

For C0=0, output bits are C2 S1 S0.
