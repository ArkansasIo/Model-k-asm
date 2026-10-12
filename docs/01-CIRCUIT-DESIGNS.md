# Model K Circuit Designs

## Boolean gates

AND(A,B)=AB; OR(A,B)=A+B; NOT(A)=~A; XOR(A,B)=A~B+~AB; NAND(A,B)=~(AB); NOR(A,B)=~(A+B); XNOR(A,B)=~(A XOR B).

## Full adder

X=A XOR B; SUM=X XOR CIN; COUT=(A AND B) OR (CIN AND X).

## Subtractor

A-B = A + NOT(B) + 1.

## ALU

The 8-bit ALU selects ADD, SUB, AND, OR, XOR, NOT, SHL, SHR, MUL, DIV, CMP, XNOR, NAND, NOR, or PASS A.

## Memory

A record is 20 bytes (160 bits). Address = base + record_id*20 + offset, with offset in [0,19].
