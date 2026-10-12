; Model K QISA example: Grover search over 2 qubits (one marked item)
; Illustrative QISA, not a vendor-native executable binary.
QALLOC Q0, 2
H Q0[0]
H Q0[1]
; Oracle for marked state |11>: phase flip only |11>
CZ Q0[0], Q0[1]
; Diffusion operator H-X-CZ-X-H
H Q0[0]
H Q0[1]
X Q0[0]
X Q0[1]
CZ Q0[0], Q0[1]
X Q0[0]
X Q0[1]
H Q0[0]
H Q0[1]
MEASURE Q0[0], C0[0]
MEASURE Q0[1], C0[1]
HALT
