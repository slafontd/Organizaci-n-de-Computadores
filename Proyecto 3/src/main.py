# Archivo principal del assembler. Se encarga de leer el archivo .asm, procesar cada instrucción y generar el archivo .hack en formato binario. Coordina el uso del parser, la tabla de símbolos y la traducción de instrucciones.

import sys
from parser import *
from code import comp_table, dest_table, jump_table, to_binary
from symbol_table import SymbolTable


def assemble(file):
    with open(file) as f:
        lines = f.readlines()

    table = SymbolTable()
    output = []

    for i, line in enumerate(lines):
        line = clean(line)
        if not line:
            continue

        # A-instruction
        if is_A(line):
            value = line[1:]

            if value.isdigit():
                output.append(to_binary(value))
            else:
                if not table.contains(value):
                    table.add_variable(value)
                output.append(to_binary(table.get(value)))

        # C-instruction
        else:
            dest, comp, jump = parse_C(line)

            if comp not in comp_table:
                raise Exception(f"Error línea {i+1}: {comp}")

            binary = "111" + comp_table[comp] + dest_table.get(dest) + jump_table.get(jump)
            output.append(binary)

    out = file.replace(".asm", ".hack")

    with open(out, "w") as f:
        f.write("\n".join(output))

    print("OK:", out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py archivo.asm")
        sys.exit(1)

    assemble(sys.argv[1])
