# Model QK Compiled Output Directory

**Directory ID:** QK-OUT-EX-0001  
**Version:** QK.2.0.0

This directory is the designated staging area for compiled executable artifacts produced from the Model QK source tree.

## Policy

- Source code remains under `asm/`, `rtl/`, `compile/`, `shell/`, `update/`, and `quantum/`.
- Generated native executables and simulation binaries belong under `output/ex/`.
- Generated binaries are build products, not authoritative source.
- The directory may contain platform-specific executable extensions such as `.exe`, ELF binaries, or test executables.
- Release artifacts should carry a version/build identifier.

## Standard artifacts

| Artifact | Producer | Purpose |
|---|---|---|
| `model_k` | `compile/Makefile` | Legacy C reference executable |
| `model_qk` | Model QK native build | 64-bit QK reference executable |
| `model_k_tb` | Root `Makefile` | SystemVerilog simulation executable |

## Build flow

`source -> compile -> output/ex -> test -> package/release`

Do not hand-edit generated binaries. Rebuild them from the corresponding source.
