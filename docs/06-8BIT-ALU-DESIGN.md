# Model K 8-bit ALU

Inputs: A[7:0], B[7:0], OP[3:0]. Outputs: Y[7:0], Carry, Zero, Negative, Overflow.

| OP | Function |
|---:|---|
| 0 | ADD |
| 1 | SUB |
| 2 | AND |
| 3 | OR |
| 4 | XOR |
| 5 | NOT A |
| 6 | SHL |
| 7 | SHR |
| 8 | MUL |
| 9 | DIV |
| A | CMP |
| B | XNOR |
| C | NAND |
| D | NOR |
| E | PASS A |

MUL and DIV are combinational reference operations; iterative multi-cycle units may reduce hardware area.
