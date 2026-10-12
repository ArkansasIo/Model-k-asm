# Model K Algorithms

- **Add:** ripple carry from bit 0 through bit 7.
- **Subtract:** invert B and add one, then add A.
- **Multiply:** shift/add; add the shifted multiplicand when multiplier bit 0 is set, then shift multiplicand left and multiplier right.
- **Divide:** repeated subtraction; quotient increments while remainder >= divisor. Divisor must be nonzero.
- **Compare:** equality when XOR(A,B)==0; unsigned ordering can be derived from subtraction/carry.
- **Record address:** base + record_id*20 + offset.
- **Checksum:** sum bytes 0 through 18 modulo 256.
