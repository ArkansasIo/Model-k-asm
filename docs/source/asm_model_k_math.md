# asm/model_k_math.asm

**File ID:** QK-ASM-0001-FILE-0003  
**Project:** Model QK — Aethernox Paradox Core  
**Version:** QK.2.0.0  
**Source path:** `asm/model_k_math.asm`

## Purpose
Implements fixed-width arithmetic and Boolean-oriented mathematical primitives used by the legacy CPU model.

## Source role
**Legacy arithmetic**

This document is the contract and maintenance record for the corresponding source file. The source remains authoritative for implementation behavior; this document records the intended architecture and verification obligations.

## Dependencies
Model K 8-bit/20-bit logical conventions.

## Interface
Assembly operands and status flags.

## Invariants
- Arithmetic width and carry/borrow semantics are part of the compatibility contract.
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
