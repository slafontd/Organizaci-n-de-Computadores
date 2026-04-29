# Se encarga de procesar cada línea del archivo de entrada. Elimina comentarios y espacios, identifica el tipo de instrucción (A o C) y separa sus componentes (dest, comp, jump).


def clean(line):
    line = line.split("//")[0]
    return line.strip()


def is_label(line):
    return line.startswith("(") and line.endswith(")")


def get_label(line):
    return line[1:-1]


def is_A(line):
    return line.startswith("@")


def parse_C(line):
    dest = None
    jump = None

    if "=" in line:
        dest, line = line.split("=")

    if ";" in line:
        line, jump = line.split(";")

    comp = line.strip()
    return dest, comp, jump