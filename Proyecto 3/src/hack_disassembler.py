# Programa encargado de convertir archivos .hack (binario) a código ensamblador .asm. Interpreta cada instrucción binaria y reconstruye su equivalente en lenguaje Hack, incluyendo soporte para operaciones de desplazamiento (shift).

import sys

dest_table = {
    "000": "",
    "001": "M",
    "010": "D",
    "011": "MD",
    "100": "A",
    "101": "AM",
    "110": "AD",
    "111": "AMD"
}

jump_table = {
    "000": "",
    "001": "JGT",
    "010": "JEQ",
    "011": "JGE",
    "100": "JLT",
    "101": "JNE",
    "110": "JLE",
    "111": "JMP"
}

comp_table = {
    "0101010": "0",
    "0111111": "1",
    "0111010": "-1",
    "0001100": "D",
    "0110000": "A",
    "1110000": "M",
    "1000010": "D+M",
    "0000010": "D+A",

    # SHIFT
    "0100000": "D<<1",
    "0100001": "D>>1",
    "0100010": "M<<1",
    "0100011": "M>>1"
}

def parse_A(binary):
    value = int(binary[1:], 2)
    return "@" + str(value)

def parse_C(binary):
    comp_bits = binary[3:10]
    dest_bits = binary[10:13]
    jump_bits = binary[13:16]

    comp = comp_table.get(comp_bits, "???")
    dest = dest_table.get(dest_bits, "")
    jump = jump_table.get(jump_bits, "")

    result = ""

    if dest != "":
        result += dest + "="

    result += comp

    if jump != "":
        result += ";" + jump

    return result

def disassemble(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    output = []

    for i, line in enumerate(lines):
        line = line.strip()

        if line == "":
            continue

        if len(line) != 16:
            raise Exception("Error línea " + str(i+1) + ": no es binario válido")

        if line[0] == "0":
            output.append(parse_A(line))

        elif line.startswith("111"):
            output.append(parse_C(line))

        else:
            raise Exception("Error línea " + str(i+1) + ": instrucción desconocida")

    out_file = input_file.replace(".hack", "Dis.asm")

    with open(out_file, "w") as f:
        f.write("\n".join(output))

    print("OK:", out_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python hack_disassembler.py archivo.hack")
        sys.exit(1)

    disassemble(sys.argv[1])