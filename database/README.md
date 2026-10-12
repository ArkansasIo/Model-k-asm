# Model K Database Records

The Excel workbook `model_k_database_records.xlsx` defines the Model K fixed 20-byte record database.

## Repository data-table export

`model_k_database_records.csv` is the portable CSV export of the primary `ModelKRecords` table.

## Record layout

| Offset | Field | Width |
|---:|---|---:|
| 0 | RecordID | 1 byte |
| 1 | Type | 1 byte |
| 2 | Flags | 1 byte |
| 3 | Version | 1 byte |
| 4 | Status | 1 byte |
| 5–18 | Payload | 14 bytes |
| 19 | Checksum | 1 byte |

Total record size: **20 bytes**.

Checksum reference: `checksum = (sum(bytes 0..18)) AND 0xFF`.
