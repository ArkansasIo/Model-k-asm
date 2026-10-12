; Model K 20-bit logical record support
; Generic 8-bit assembly model.
; R0 = bits 7..0, R1 = bits 15..8, R2 low nibble = bits 19..16.
; 20-bit mask = 0x0FFFFF.

MK20_MASK:
    AND R2, #0x0F
    RET

MK20_ADD:
    ADD R0, R3
    ADC R1, R4
    ADC R2, R5
    AND R2, #0x0F
    RET

MK20_XOR:
    XOR R0, R3
    XOR R1, R4
    XOR R2, R5
    AND R2, #0x0F
    RET

MK20_AND:
    AND R0, R3
    AND R1, R4
    AND R2, R5
    AND R2, #0x0F
    RET

MK20_OR:
    OR R0, R3
    OR R1, R4
    OR R2, R5
    AND R2, #0x0F
    RET

MK20_NOT:
    XOR R0, #0xFF
    XOR R1, #0xFF
    XOR R2, #0xFF
    AND R2, #0x0F
    RET

MK20_COMPARE:
    CMP R2, R5
    BNE MK20_COMPARE_DONE
    CMP R1, R4
    BNE MK20_COMPARE_DONE
    CMP R0, R3
MK20_COMPARE_DONE:
    RET

; Store the logical 20-bit value in bytes 0..2 of a 20-byte physical record.
MK20_STORE:
    STORE [RP+0], R0
    STORE [RP+1], R1
    AND R2, #0x0F
    STORE [RP+2], R2
    RET

; Fixed 20-byte record address: BASE + record_id*20.
; 20*n = (n<<4) + (n<<2).
MK20_ADDRESS:
    MOV R6, R7
    SHL R6, 4
    MOV R5, R7
    SHL R5, 2
    ADD R6, R5
    ADD R6, R4
    RET