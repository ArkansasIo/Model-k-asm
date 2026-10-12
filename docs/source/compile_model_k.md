# compile/src/model_k.c

**File ID:** QK-CMP-0001-FILE-0001  
**Project:** Model QK — Aethernox Paradox Core  
**Version:** QK.2.0.0  
**Source path:** `compile/src/model_k.c`

## Purpose
Software reference implementation used to cross-check the legacy architecture.

## Source role
**Legacy C reference**

This document is the contract and maintenance record for the corresponding source file. The source remains authoritative for implementation behavior; this document records the intended architecture and verification obligations.

## Dependencies
Legacy Model K data types and arithmetic.

## Interface
C functions and deterministic return values.

## Invariants
- Must remain compatible with the documented legacy architecture.
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
