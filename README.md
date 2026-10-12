# Model K — 8-bit Assembly and Unified Circuit Design

This repository contains the Model K reference implementation package: an 8-bit datapath, K2 two-bit adder, logic gate primitives, ALU, CPU/register/control design, 20-byte record memory, assembly algorithm examples, equations, circuit documentation, and a SystemVerilog testbench.

## Package

Download `model-k-unified-circuit.zip` from this repository and extract it to obtain the complete source tree (`rtl/`, `asm/`, `tb/`, `docs/`, and `Makefile`).

## Quick test

With Icarus Verilog installed, run:

```sh
make test
```

This is an educational RTL reference design; verify and adapt the CPU instruction/control semantics before treating it as production silicon or a finished FPGA implementation.
