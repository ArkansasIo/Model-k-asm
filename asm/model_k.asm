; MODEL K reference assembly (pseudo-assembly for the documented ISA)
; 8-bit datapath; 20-byte record layout is documented in docs/03-20-BYTE-RECORD.md
ADD8:  ADD R0,R1
       RET
SUB8:  SUB R0,R1
       RET
XOR8:  XOR R0,R1
       RET
AND8:  AND R0,R1
       RET
OR8:   OR R0,R1
       RET
; Shift/add multiply
MUL8:  MOV R2,#0
MUL_LOOP:
       AND R3,R1,#1
       CMP R3,#0
       BEQ MUL_SKIP
       ADD R2,R0
MUL_SKIP:
       SHL R0,#1
       SHR R1,#1
       CMP R1,#0
       BNE MUL_LOOP
       MOV R0,R2
       RET
; Repeated-subtraction division; divisor must be nonzero
DIV8:  MOV R2,#0
DIV_LOOP:
       CMP R0,R1
       BLT DIV_DONE
       SUB R0,R1
       ADD R2,#1
       JMP DIV_LOOP
DIV_DONE:
       MOV R1,R0
       MOV R0,R2
       RET
