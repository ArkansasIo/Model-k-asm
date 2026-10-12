# Aethernox v2 — 64-bit Logical Data Architecture

**Status:** Proposed specification, version 2.0  
**Date:** 11 October 2026  
**Compatibility:** Model K v1 remains available as a legacy reference.

## 1. Terminology

- **Datapath width:** number of bits processed directly by the CPU datapath in one operation.
- **Logical value width:** width of an architectural integer or value type.
- **Physical record size:** number of bytes used to serialize one record.
- **Address width:** width of an address or address-like identifier.

Aethernox v2 initially defines a **64-bit logical value**. This does not make the existing 8-bit CPU a native 64-bit CPU. On the existing CPU, 64-bit operations are implemented as multi-byte routines. A separate native 64-bit datapath is an optional later hardware variant.

## 2. Integer semantics

Unsigned 64-bit values satisfy:

`0 <= x <= 2^64 - 1`

Maximum unsigned value: `18,446,744,073,709,551,615`.

For modular arithmetic, results wrap modulo `2^64`. Operations that need checked arithmetic shall return carry/overflow/error status rather than silently changing the specified policy. Signed integers use two's-complement representation, range `-2^63` through `2^63 - 1`.

## 3. Recommended fixed record format

Aethernox v2 uses a 32-byte fixed header record for the initial binary table format. Payloads may be fixed-width or length-delimited at the table-format layer; do not append arbitrary data to a fixed record without a versioned format.

### 64-byte record v2

| Offset | Width | Field | Meaning |
|---:|---:|---|---|
| 0 | 4 | RecordID | Unsigned 32-bit identifier, little-endian |
| 4 | 2 | RecordType | Unsigned 16-bit schema/type identifier |
| 6 | 2 | Flags | Versioned bit flags |
| 8 | 2 | SchemaVersion | Record schema version |
| 10 | 2 | Status | Record lifecycle/status |
| 12 | 8 | LogicalValue | Unsigned 64-bit value, little-endian |
| 20 | 4 | PayloadLength | Number of meaningful payload bytes, 0–35 |
| 24 | 35 | Payload | Application-defined bytes, zero-padded if fixed-width |
| 59 | 4 | Reserved | Must be zero in v2.0 |
| 63 | 1 | Checksum8 | Sum of bytes 0–62 modulo 256 |

**Total: 64 bytes.** This is a proposed new format and does not overwrite the legacy 20-byte record definition. Note: payload length must be <=35; reserved bytes must be zero for v2.0.

## 4. Table header

Recommended table header: 32 bytes.

| Offset | Width | Field |
|---:|---:|---|
| 0 | 4 | Magic: `AKT2` |
| 4 | 2 | FormatVersion: 2 |
| 6 | 2 | HeaderSize: 32 |
| 8 | 2 | RecordSize: 64 |
| 10 | 2 | Flags |
| 12 | 4 | RecordCount |
| 16 | 8 | MasterSeed |
| 24 | 4 | SchemaID |
| 28 | 4 | HeaderChecksum |

The table format must define checksum coverage and endian encoding in its implementation tests. For v2.0, use little-endian integers and a 32-bit additive header checksum over bytes 0–27, modulo 2^32. A future cryptographic integrity layer may add a digest/signature; an additive checksum is for accidental corruption detection only, not security.

## 5. Memory backend abstraction

Define a backend contract:

- `read(address, length) -> bytes/status`
- `write(address, bytes) -> status`
- `flush() -> status`
- `capabilities() -> flags`
- `diagnostics() -> metrics`

Backends:
- `BRAM_SRAM`: low-latency working storage.
- `DRAM`: main memory, with refresh and controller timing handled by the controller.
- `NAND_NVME`: persistent block storage; use a standard host/storage interface where available.
- `MRAM`: optional non-volatile memory research backend.
- `FERRITE_CORE_LAB`: historical experimental backend, explicitly labelled laboratory-only.

Do not imply that all backends have identical latency, endurance, atomicity, or persistence semantics. Capabilities must be queried and tests must account for each backend.

## 6. Compatibility and migration

- Model K v1 keeps its 8-bit datapath, 20-bit logical values, and legacy record formats.
- Aethernox v2 introduces 64-bit logical values and the 64-byte record schema above.
- Migration is explicit: parse v1 using its own schema, validate it, map fields into v2, and write a new v2 record. Never reinterpret v1 bytes in place.
- The current repository contains more than one historical 20-byte layout. Assign distinct schema IDs before implementing automatic conversion.
- The quantum subsystem remains out of scope and unchanged by this migration.

## 7. Acceptance tests

1. Encode/decode 0, 1, 2^32−1, 2^32, 2^63−1, and 2^64−1.
2. Reject payload length >35.
3. Verify the exact 64-byte serialized length.
4. Verify checksum behavior for all 64 byte positions.
5. Reject unknown schema versions unless an explicit compatibility handler exists.
6. Verify v1 → v2 conversion preserves mapped values and records migration provenance.
7. Test interrupted writes and corrupted records separately for volatile and persistent backends.
8. Cross-check C, ASM reference routines, and RTL test vectors wherever an implementation exists.
