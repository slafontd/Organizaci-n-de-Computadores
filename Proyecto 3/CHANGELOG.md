CHANGELOG - Proyecto 3 (Assembler y Disassembler con Shift)

Autor: Santiago Lafont Díaz
Fecha: 29/04/2026

---

Versión 1.0

* Se implementó un assembler que traduce código ASM a binario (.hack)
* Se soportan instrucciones tipo A (@valor)
* Se soportan instrucciones tipo C (dest=comp;jump)
* Se implementó limpieza de comentarios y líneas vacías
* Se desarrolló una tabla de símbolos para variables y etiquetas
* Se asignan direcciones automáticamente a variables desde la posición 16

---

Extensión: SHIFT

* Se añadieron operaciones de desplazamiento:

  * Shift Left (<<)
  * Shift Right (>>)
* Se definieron nuevos códigos en el campo comp
* Compatible con la CPU extendida del proyecto 2

---

Disassembler

* Se implementó un programa que traduce de binario (.hack) a ASM
* Reconstruye instrucciones tipo A y tipo C
* Soporta también instrucciones de desplazamiento (shift)

---

Estructura del proyecto

* main.py → assembler
* parser.py → análisis de instrucciones
* code.py → traducción a binario
* symbol_table.py → manejo de símbolos
* hack_disassembler.py → conversión inversa

---

Notas

* El sistema traduce correctamente en ambas direcciones
* Se validó con múltiples archivos de prueba
