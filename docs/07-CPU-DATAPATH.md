# Model K CPU Datapath

```text
PC -> Instruction Input/Register -> Decoder/Control
                                 -> Register File R0..R7
                                 -> ALU -> Writeback -> Register File
```

The reference CPU uses a compact one-instruction-per-clock model. The supplied assembly is pseudo-assembly for the intended ISA and is not yet a machine-code assembler implementation.
