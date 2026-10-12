; Model K QISA educational teleportation skeleton
; Q0[0]=unknown input |psi>, Q0[1]=Alice half of Bell pair, Q0[2]=Bob half.
; Classical feed-forward uses measured bits; requires simulator/runtime support.
QALLOC Q0, 3
H Q0[1]
CX Q0[1], Q0[2]
CX Q0[0], Q0[1]
H Q0[0]
MEASURE Q0[0], C0[0]
MEASURE Q0[1], C0[1]
IF C0[1] == 1 THEN X Q0[2]
IF C0[0] == 1 THEN Z Q0[2]
; Q0[2] now carries the input state up to noise/runtime semantics.
HALT
