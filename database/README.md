# Model K / Aethernox Database Records

## Model K v1 legacy format

The existing `model_k_database_records.xlsx` and `model_k_database_records.csv` define the Model K fixed 20-byte record schema. Keep these formats available for compatibility.

| Offset | Field | Width |
|---:|---|---:|
| 0 | RecordID | 1 byte |
| 1 | Type | 1 byte |
| 2 | Flags | 1 byte |
| 3 | Version | 1 byte |
| 4 | Status | 1 byte |
| 5–18 | Payload | 14 bytes |
| 19 | Checksum | 1 byte |

Total: **20 bytes**. Checksum reference: `checksum = (sum(bytes 0..18)) AND 0xFF`.

The repository also contains a computation-oriented 20-byte test-record layout in `docs/03-20-BYTE-RECORD.md`. These layouts are not interchangeable; a reader must know which schema it is decoding.

## Aethernox v2 proposal

See [RECORD_FORMAT_V2.md](RECORD_FORMAT_V2.md) for the proposed 64-byte record with a 64-bit logical value. V2 uses explicit schema versioning and little-endian multi-byte fields. It is a new format and does not overwrite v1.

A v1-to-v2 converter must be schema-aware, validate source checksums, preserve migration provenance, and write new records rather than modifying the original bytes in place.