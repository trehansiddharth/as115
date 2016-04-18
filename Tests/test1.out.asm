; Main file for this project

; ==== Included from "test1.h.asm" by AS115: ====
; Header file that defines all the register memonics

.equ led, 90h

.org 0000h
sjmp main

.org 0050h
main:
    lcall delay
    lcall blinkled
    sjmp main

; ==== Included from "util.lib.asm" by AS115: ====
; Some utility subroutines that we want to include in our main asm file

delay:
    mov r0, #0ffh
    delay_loop:
        djnz r0, delay_loop
    ret

blinkled:
    cpl led
    ret
