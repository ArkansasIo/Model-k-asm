# rtl/model_k.sv

**File ID:** QK-RTL-0001-FILE-0001  
**Project:** Model QK — Aethernox Paradox Core  
**Version:** QK.2.0.0  
**Source path:** `rtl/model_k.sv`

## Purpose
Structural/SystemVerilog reference for the Model K processor datapath and control integration.

## Source role
**Legacy RTL top**

This document is the contract and maintenance record for the corresponding source file. The source remains authoritative for implementation behavior; this document records the intended architecture and verification obligations.

## Dependencies
Boolean gates, adders, ALU, registers, memory and CPU modules.

## Interface
Clock/reset and RTL signals.

## Invariants
- Synthesizable intent must remain separate from behavioral testbench code.
- Errors and unsupported operations should be explicit rather than silently coerced.
- Changes that alter the public contract require a versioned documentation update.

## Verification
- Build or import the source in its native toolchain.
- Exercise the documented public entry points.
- Run the relevant repository test suite.
- Record failures as implementation issues rather than weakening the contract.

## Compatibility
Model QK is the current architecture. Legacy Model K identifiers and implementations remain compatibility references where applicable; they are not implicitly redefined by this source.

## Change record
- QK.2.0.0 — source-specific contract created for the per-file documentation layer.
