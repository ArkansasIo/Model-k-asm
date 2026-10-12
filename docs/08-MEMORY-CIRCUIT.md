# Model K Memory Circuit

Byte-addressed memory with 20-byte records.

record_base = record_id * 20
address = record_base + offset

Memory size for 256 records: 256*20 = 5120 bytes.

Interface: clock, write enable, 16-bit address, 8-bit write data, 8-bit read data.
