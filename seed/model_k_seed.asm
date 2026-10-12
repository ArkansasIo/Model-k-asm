; Model K deterministic seed primitives
; Portable reference assembly; backend-specific implementation may replace mixing.

SEED_INIT:
    ; R0:R7 contain the 64-bit seed
    ; R8 contains the domain/stream identifier
    XOR R0, R8
    XOR R1, R8
    XOR R2, R8
    XOR R3, R8
    RET

SEED_NEXT:
    ADD R0, #0xB9
    ADC R1, #0x79
    ADC R2, #0x37
    ADC R3, #0x9E
    RET
