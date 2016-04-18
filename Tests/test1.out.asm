; Included from "test1.h.asm" by AS115:
.equ led, 90h

.org 0000h
sjmp main

.org 0050h
main:
    lcall delay
    lcall blinkled
    sjmp main

; Included from "util.lib.asm" by AS115:
delay:
    mov r0, #0ffh
    delay_loop:
        djnz r0, delay_loop
    ret

blinkled:
    cpl led
    ret
