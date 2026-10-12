# Aethernox v2 Record Format

**Version:** 2.0 — proposed  
**Effective date:** 11 October 2026

The legacy Model K database format remains unchanged for compatibility. This document defines a separate 64-byte Aethernox v2 record with a 64-bit logical value.

| Offset | Bytes | Field | Rules |
|---:|---:|---|---|
| 0 | 4 | RecordID | Unsigned 32-bit little-endian |
| 4 | 2 | RecordType | Unsigned 16-bit little-endian |
| 6 | 2 | Flags | Bitfield |
| 8 | 2 | SchemaVersion | Must be supported by reader |
| 10 | 2 | Status | Defined by record type |
| 12 | 8 | LogicalValue | Unsigned 64-bit little-endian |
| 20 | 4 | PayloadLength | 0–35 |
| 24 | 35 | Payload | Bytes; zero padding in fixed record |
| 59 | 4 | Reserved | Zero in v2.0 |
| 63 | 1 | Checksum8 | Sum of bytes 0–62 modulo 256 |

Record size is exactly 64 bytes. Checksum8 detects some accidental corruption; it is not a cryptographic integrity mechanism.

## Example serialization rules

- All multi-byte integers are little-endian.
- The reader validates exact record length, schema version, payload length, reserved bytes, and checksum before returning a record.
- Unknown record types are rejected or returned as opaque records only when the caller explicitly requests that policy.
- A record with invalid checksum must not be committed to persistent storage.
- Record IDs must be treated as identifiers, not raw memory pointers.

## Relationship to legacy records

The repository's existing 20-byte schemas are retained as v1 compatibility formats. There are multiple historical layouts in the project; conversion must use a declared source schema ID. A migration tool must not guess which layout a 20-byte record uses.
