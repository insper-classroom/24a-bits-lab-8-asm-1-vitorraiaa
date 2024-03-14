; Arquivo: exe1.nasm
; Salva 5 na RAM[10]

leaw $5, %A
movw %A, %D
leaw $10, %A
movw %D, (%A)