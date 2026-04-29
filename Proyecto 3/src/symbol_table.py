# Implementa la tabla de símbolos. Almacena los símbolos predefinidos, etiquetas y variables, y asigna direcciones de memoria cuando es necesario.


class SymbolTable:
    def __init__(self):
        self.table = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576
        }

        for i in range(16):
            self.table[f"R{i}"] = i

        self.next_var = 16

    def add(self, symbol, address):
        self.table[symbol] = address

    def get(self, symbol):
        return self.table.get(symbol)

    def contains(self, symbol):
        return symbol in self.table

    def add_variable(self, symbol):
        self.table[symbol] = self.next_var
        self.next_var += 1