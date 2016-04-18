; Some utility subroutines that we want to include in our main asm file

delay:
    mov r0, #0ffh
    delay_loop:
        djnz r0, delay_loop
    ret

blinkled:
    cpl led
    ret
