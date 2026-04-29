CHANGELOG - Proyecto 2 (Arquitectura del Computador)

Autor: Santiago Lafont Díaz
Fecha: 29/04/2026

Versión 1.0

Implementación de los componentes principales del computador Hack
según el proyecto 5 de Nand2Tetris.

Memory.hdl

Se implementó la memoria principal del sistema
Incluye:
RAM16K
Screen
Keyboard
Se realizó el mapeo correcto de direcciones:
RAM: 0 - 16383
Screen: 16384 - 24575
Keyboard: 24576
Se validó mediante pruebas manuales y simulación

CPU.hdl

Se implementó la CPU basada en:
Registro A
Registro D
ALU
PC (Program Counter)
Se manejan instrucciones tipo A y tipo C
Se implementó lógica de saltos (jump)
Se integró la ALU desarrollada previamente
Se añadieron operaciones extendidas de desplazamiento:
Shift Left (<<)
Shift Right (>>)

Computer.hdl

Se integró la CPU con el módulo Memory
Se conectaron correctamente:
inM, outM, writeM
addressM
pc
Se validó ejecutando programas en formato .hack
Se probó con programas que interactúan con:
Screen
Keyboard

Pruebas realizadas

Pruebas unitarias de Memory
Pruebas unitarias de CPU (CPU.tst)
Ejecución de programas completos en Computer
Validación visual del funcionamiento de Screen
Validación de entrada por Keyboard

Notas

Todos los módulos funcionan correctamente en la plataforma Nand2Tetris
El sistema es capaz de ejecutar programas completos sin errores
