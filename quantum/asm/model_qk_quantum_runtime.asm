; Model QK Quantum Runtime
; QISA-compatible assembly reference. Classical host controls the quantum backend.
; This is a specification/reference program, not direct physical-device code.

QKQ_BOOT:
    QALLOC   Q0, 2
    RESET    Q0
    RESET    Q1
    HALT

QKQ_BELL:
    H        Q0
    CX       Q0, Q1
    MEASURE  Q0, R0
    MEASURE  Q1, R1
    HALT

QKQ_SHUTDOWN:
    QFREE    Q0
    QFREE    Q1
    HALT
