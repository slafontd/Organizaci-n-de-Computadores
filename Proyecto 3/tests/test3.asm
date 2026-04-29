@10
D=A
@i
M=D

(LOOP)
@i
D=M
D=D<<1
@END
D;JEQ
@LOOP
0;JMP

(END)
@0
M=D
