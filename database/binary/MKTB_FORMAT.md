# MKTB v1 Format

Header: 32 bytes. Magic 0..3; version 4..5; record size 6..7; record count 8..11; table flags 12..15; master seed 16..23; reserved 24..31.

Record: exactly 20 bytes. Record ID 0..3; type 4; flags 5; record version 6; status 7; 20-bit value 8..10; payload 11..18; checksum 19.

Numeric fields are little-endian. Reference checksum is the sum of bytes 0..18 modulo 256.
