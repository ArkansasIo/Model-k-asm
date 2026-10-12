# compile/src/model_qk.c

**File ID:** QK-CMP-0001-FILE-0002  
**Project:** Model QK — Aethernox Paradox Core  
**Version:** QK.2.0.0  
**Source path:** `compile/src/model_qk.c`

## Purpose
Implements Aethernox/Model QK 64-bit arithmetic and record integrity primitives.

## Source role
**64-bit QK C reference**

This document is the contract and maintenance record for the corresponding source file. The source remains authoritative for implementation behavior; this document records the intended architecture and verification obligations.

## Dependencies
compile/include/model_qk.h.

## Interface
uint64_t arithmetic and QKRecord validation.

## Invariants
- Logical values are 64-bit while the physical record format is fixed at 64 bytes.
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
