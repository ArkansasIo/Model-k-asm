# 64-bit Logical Operations on the 8-bit Model K

**Status:** Design contract; not yet a complete executable instruction set.

The existing CPU datapath is 8-bit. A 64-bit logical integer is represented as eight ordered bytes. This provides 64-bit values without claiming the processor is natively 64-bit.

## Register/byte convention

Use `B0` as the least-significant byte and `B7` as the most-significant byte. Serialized values use little-endian byte order. Any future assembler syntax must document how these byte names map to actual registers or memory locations.

## Addition

For each byte i from 0 through 7:

- `sum_i = a_i + b_i + carry_i`
- `result_i = sum_i AND 0xFF`
- `carry_(i+1) = floor(sum_i / 256)`

Final carry indicates unsigned overflow.

## Subtraction

Use two's complement: `A - B = A + NOT(B) + 1`, propagated byte-by-byte. Define carry/borrow convention once and test it across all routines.

## Comparison

Compare B7 down to B0 for unsigned comparison. Signed comparison must interpret the sign bit of B7 and must be implemented as a distinct operation or explicitly specified routine.

## Required routines

- `U64_ADD`
- `U64_SUB`
- `U64_CMP`
- `U64_INC`
- `U64_DEC`
- `U64_AND`
- `U64_OR`
- `U64_XOR`
- `U64_NOT`
- `U64_SHIFT_LEFT`
- `U64_SHIFT_RIGHT_LOGICAL`
- `U64_LOAD_LE`
- `U64_STORE_LE`
- `U64_CHECKED_ADD`

These names are proposed interface labels until each routine is implemented and tested.

## Test vectors

- 0 + 0 = 0
- (2^64 − 1) + 1 = 0 with carry
- 0 − 1 = 2^64 − 1 with borrow/underflow
- 0x0000000100000000 + 1 = 0x0000000100000001
- 0x7FFFFFFFFFFFFFFF + 1 = 0x8000000000000000 with signed overflow
- Little-endian encoding of 0x0123456789ABCDEF is EF CD AB 89 67 45 23 01

The 64-bit routines must not be presented as implemented until executable code and tests exist.
