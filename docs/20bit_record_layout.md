# Model K 20-Bit Logical Record

A 20-bit value uses three 8-bit registers:
VALUE20 = R0 + 256*R1 + 65536*(R2 AND 0x0F)

The upper four bits of R2 are reserved and zero.

The existing physical record remains 20 bytes (160 bits). Bytes 0..2 carry the logical value:
byte 0 = bits 0..7
byte 1 = bits 8..15
byte 2 low nibble = bits 16..19

The remaining 17 bytes are metadata, payload, and integrity storage.