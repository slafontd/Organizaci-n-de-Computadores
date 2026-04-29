# Contiene las tablas de traducción que convierten las partes de una instrucción en su representación binaria. Incluye soporte para instrucciones normales y operaciones extendidas de desplazamiento (shift).

dest_table = {
    None: "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

jump_table = {
    None: "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

comp_table = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "D+M": "1000010",
    "D+A": "0000010",

    # SHIFT
    "D<<1": "0100000",
    "D>>1": "0100001",
    "M<<1": "0100010",
    "M>>1": "0100011",
}


def to_binary(n):
    return format(int(n), "016b")