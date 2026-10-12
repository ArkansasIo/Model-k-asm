# Model QK — Project Rename

**Effective:** 11 October 2026

The project formerly presented as **Model K** is now named **Model QK**.

## Naming policy

- **Public project name:** Model QK
- **Expanded name:** Model QK — Aethernox Paradox Core
- **Legacy implementation namespace:** mk_, MK*, and model_k* remain valid compatibility identifiers until a separately versioned API migration is completed.
- **Quantum interface:** QISA remains the project-defined quantum instruction layer; its semantics are not changed by the rename.
- **Repository path:** ArkansasIo/Model-k-asm is retained for Git history and existing clones. A GitHub repository rename can be performed separately through repository settings without rewriting source identifiers.

## Why compatibility identifiers remain

Renaming every source symbol and filename in one change would break Makefiles, RTL module references, include paths, scripts, examples, and downstream users. Model QK therefore separates product branding from ABI/source compatibility.

New code should use Model QK in documentation and user-facing interfaces. New APIs should prefer a qk_ namespace when an ABI break is intentionally scheduled.

## Version identity

- Model K v1: legacy architecture and compatibility baseline.
- Aethernox v2: 64-bit logical-data architecture.
- Model QK: current project/product name spanning the classical and quantum research layers.

The rename does not claim that the quantum subsystem is physical hardware; simulator, interface, and physical-device claims remain explicitly separated.
