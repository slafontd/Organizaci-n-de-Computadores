# Proyecto 2 – Arquitectura del Computador Hack
**Organización de computadores**
** 2026-1**
**Integrantes proyecto 2**
[Santiago Lafont Díaz]

## Descripción

En este proyecto se implementa la arquitectura completa del computador Hack utilizando HDL en la plataforma Nand2Tetris. Se desarrollan los módulos principales del sistema: memoria, CPU y computador, permitiendo la ejecución de programas en lenguaje máquina.

---

## Componentes implementados}


## Shifter

Se implementó un módulo adicional para realizar desplazamientos de bits
Permite:
Desplazamiento a la izquierda
Desplazamiento a la derecha
Se integra con la ALU para producir el resultado final cuando se detecta una operación de shift

---

### Memory.hdl

* Implementación de la memoria del sistema
* Incluye:

  * RAM16K
  * Screen
  * Keyboard
* Mapeo de direcciones:

  * RAM: 0 – 16383
  * Screen: 16384 – 24575
  * Keyboard: 24576

---

### CPU.hdl

* Implementación de la unidad central de procesamiento
* Componentes:

  * Registro A
  * Registro D
  * ALU
  * Program Counter (PC)
* Soporte para:

  * Instrucciones tipo A y C
  * Operaciones aritméticas y lógicas
  * Saltos (jump)
* Extensión implementada:

  * Shift Left (<<)
  * Shift Right (>>)

---

### Computer.hdl

* Integración de CPU y Memory
* Permite la ejecución de programas completos
* Manejo de:

  * Entrada (Keyboard)
  * Salida (Screen)

---

## Pruebas realizadas

* Pruebas unitarias de Memory
* Pruebas unitarias de CPU (CPU.tst)
* Ejecución de programas en Computer
* Validación visual del Screen
* Interacción con Keyboard

---

## Estructura del proyecto

proyecto2/
├── Shifter.hdl
├── Memory.hdl
├── CPU.hdl
├── Computer.hdl
├── CHANGELOG.txt
├── LICENSE.txt
└── README.md


---

## Requisitos

* Plataforma Nand2Tetris (web o desktop)
* Archivos de prueba del proyecto 5

---

## Notas

* El sistema funciona correctamente en la simulación
* Se implementó una extensión de la ALU para operaciones de desplazamiento

---

## Autor

Santiago Lafont Díaz
