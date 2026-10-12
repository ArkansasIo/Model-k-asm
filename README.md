# Model K — 8-bit Assembly and Unified Circuit Design

Model K is an educational 8-bit computer reference design built from Boolean gates, a K2 two-bit adder, an 8-bit ALU, registers, a compact CPU, and byte-addressed 20-byte records.

## Source tree

- `rtl/` — SystemVerilog gate primitives, adders, ALU, registers, record memory, CPU, and top-level module
- `asm/model_k.asm` — reference pseudo-assembly algorithms
- `tb/model_k_tb.sv` — K2 adder testbench
- `docs/` — architecture, circuit equations, gate truth tables, record layout, ALU, datapath, memory, verification, and synthesis notes
- `Makefile` — Icarus Verilog test target

## Run the test

Install Icarus Verilog, then run:

```sh
make test
```

The assembly file documents the intended instruction style; it is pseudo-assembly, not yet a machine-code assembler. Review and simulate the RTL before treating it as a finished FPGA or production hardware design.
