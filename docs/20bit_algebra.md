# Model K 20-Bit Algebra and Equations

20-bit unsigned range: 0 <= x <= 2^20-1 = 1,048,575.
Mask: 0xFFFFF.

AND: Y=A B
OR: Y=A+B
NOT: Y=¬A
XOR: Y=A⊕B=A¬B+¬AB
NAND: Y=¬(AB)
NOR: Y=¬(A+B)
XNOR: Y=AB+¬A¬B

Half adder:
S=A⊕B
C=AB

Full adder:
S=A⊕B⊕Cin
Cout=AB+Cin(A⊕B)=AB+ACin+BCin

For each bit i:
S_i=A_i⊕B_i⊕C_i
C_(i+1)=A_iB_i+C_i(A_i⊕B_i)
C_0=0.

20-bit addition:
R=(A+B) mod 2^20

Subtraction:
A-B=A+(~B+1), then mask to 20 bits.

Multiplication:
R=(A*B) mod 2^20 using binary shift/add.

Division:
Use restoring or shift/subtract division from bit 19 down to bit 0.

Comparison:
Compare bit 19 first, then 18..0; the first unequal bit determines unsigned ordering.