; Model K mathematical primitives
; 20-bit values use R0:R2; R2 low nibble is significant.
ADD20: ADD R0, R3
 ADC R1, R4
 ADC R2, R5
 AND R2, #0x0F
 RET
SUB20: SUB R0, R3
 SBC R1, R4
 SBC R2, R5
 AND R2, #0x0F
 RET
MUL20_LOW: CALL MUL_WIDE
 AND R2, #0x0F
 RET
BOOL_XOR: XOR R0, R1
 RET
BOOL_AND: AND R0, R1
 RET
BOOL_OR: OR R0, R1
 RET
BOOL_NOT: NOT R0
 RET
