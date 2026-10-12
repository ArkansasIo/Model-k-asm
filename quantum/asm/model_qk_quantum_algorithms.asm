; Model QK Quantum Algorithm Library
; Reference routines. Backend-specific lowering is required before hardware execution.

QK_BELL:
    QALLOC Q0, 2
    RESET Q0
    H Q0
    CX Q0, Q1
    MEASURE Q0, R0
    MEASURE Q1, R1
    QFREE Q0
    HALT

QK_GROVER_2Q:
    QALLOC Q0, 2
    RESET Q0
    H Q0
    H Q1
    ; Oracle and diffusion are represented by the circuit fixture.
    ; Hardware compiler inserts backend-native operations.
    MEASURE Q0, R0
    MEASURE Q1, R1
    QFREE Q0
    HALT

QK_TELEPORT:
    QALLOC Q0, 3
    RESET Q0
    H Q1
    CX Q1, Q2
    CX Q0, Q1
    H Q0
    MEASURE Q0, R0
    MEASURE Q1, R1
    ; Feed-forward operations are backend/runtime controlled.
    QFREE Q0
    QFREE Q1
    QFREE Q2
    HALT
