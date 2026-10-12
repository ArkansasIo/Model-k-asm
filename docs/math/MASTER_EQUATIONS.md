# Model K Master Equations — Expanded

Boolean: NOT A=A', AND=AB, OR=A+B, XOR=A'B+AB'.

Half adder: S=A XOR B; C=AB.

Full adder: S=A XOR B XOR Cin; Cout=AB+Cin(A XOR B).

20-bit range: 0 <= x <= 2^20-1 = 1,048,575.

20-byte record = 160 bits.

MKTB address(i) = base + 32 + 20i.

Tree subtree size: size(v)=1+sum(size(c)).

Dijkstra: d(v)=min(d(v),d(u)+w(u,v)).

Quantum: |psi>=sum_i alpha_i|i>, sum_i|alpha_i|^2=1, |psi'>=U|psi>, P(i)=|alpha_i|^2.

Update state machine: CHECK -> VERIFY -> STAGE -> APPLY -> TEST -> COMMIT; failure -> ROLLBACK -> VERIFY -> RESTORE.
