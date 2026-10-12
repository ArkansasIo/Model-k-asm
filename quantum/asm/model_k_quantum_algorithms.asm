; Quantum algorithm examples
BELL:
    QALLOC Q0
    QALLOC Q1
    H Q0
    CX Q0,Q1
    MEASURE Q0 -> R0
    MEASURE Q1 -> R1
    RET

SUPERPOSITION:
    QALLOC Q0
    H Q0
    MEASURE Q0 -> R0
    RET
