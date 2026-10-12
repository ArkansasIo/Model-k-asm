# Model K Equations

8-bit word: X = sum(i=0..7) x_i * 2^i.

Addition: A+B = S + 256*C8.

Subtraction: A-B = A + NOT(B) + 1.

Multiplication: A*B = sum(i=0..7) b_i*(A*2^i).

Division: A=BQ+R, where 0<=R<B for B != 0.

Timing estimate: T = N*C/f, where N is instruction count, C is average cycles/instruction, and f is clock frequency.

Checksum: checksum = (sum(byte[0..18])) mod 256.
