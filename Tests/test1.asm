.inc test1.h.asm

.org 0000h
sjmp main

.org 0050h
main:
    lcall delay
    lcall blinkled
    sjmp main

.inc util.lib.asm
