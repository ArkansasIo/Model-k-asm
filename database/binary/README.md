# Model K Binary Table

MKTB is the physical binary table container for Model K.

- 32-byte table header
- fixed 20-byte records
- 20-bit logical values
- little-endian numeric fields
- checksum per record
- suitable for magnetic-core-backed block storage
