# Model QK Output/EX Build Artifact Specification

**Document ID:** QK-DOC-0001-OUTPUT-EX  
**Version:** QK.2.0.0

## Purpose

Define the repository convention for executable files created after compilation.

## Directory

`output/ex/` is the canonical generated-executable staging directory.

## Lifecycle

1. Source files are edited and reviewed.
2. The compiler or HDL simulator creates an executable.
3. The executable is written to `output/ex/`.
4. Tests execute the staged artifact.
5. Release packaging may copy a verified artifact elsewhere.

## Separation of concerns

The source tree contains reproducible inputs. The `output/ex` tree contains derived outputs. This prevents compiled binaries from being confused with source files or documentation.

## Naming

Recommended names are stable product names during development and versioned names for releases, for example:

- `model_k`
- `model_qk`
- `model_k_tb`
- `model_qk-2.0.0-linux-x86_64`
- `model_qk-2.0.0-windows-x86_64.exe`

## Verification

A compiled artifact is considered verified only after its producer build succeeds and its associated test target passes. The repository should record compiler/toolchain versions and commit SHA for formal releases.
