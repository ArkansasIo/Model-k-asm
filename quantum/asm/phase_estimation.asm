; Model K QISA phase-estimation teaching example
; Target U|1> = exp(2*pi*i*phi)|1>, illustrative controlled-U placeholders.
QALLOC Q0, 3
H Q0[0]
H Q0[1]
X Q0[2]
CONTROLLED_U Q0[0], Q0[2], POWER=1
CONTROLLED_U Q0[1], Q0[2], POWER=2
; Inverse QFT on the two counting qubits (expanded gates depend on backend).
SWAP Q0[0], Q0[1]
H Q0[0]
CONTROLLED_PHASE Q0[1], Q0[0], ANGLE=-PI/2
H Q0[1]
MEASURE Q0[0], C0[0]
MEASURE Q0[1], C0[1]
HALT
