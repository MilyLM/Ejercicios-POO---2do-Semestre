# Ejercicio 7: Manejo de Excepciones en Python

Este proyecto demuestra la implementación de estructuras de control de errores para gestionar situaciones excepcionales durante la ejecución de un programa. El objetivo es garantizar la robustez del software evitando cierres inesperados mediante el uso de bloques try-except.

---

## Objetivo de Aprendizaje

El propósito de esta práctica es dominar el flujo de control de excepciones en Python, comprendiendo la jerarquía de errores y el uso de cláusulas adicionales para la gestión de recursos y estados finales del programa.

---

## Estructura del Ejercicio

La práctica se divide en dos scripts principales que abordan diferentes tipos de errores comunes en el desarrollo de software.

### Parte A: Operaciones Aritméticas (excepciones_A.py)

En este script se gestionan errores derivados de la interacción con el usuario y operaciones matemáticas:

* **ValueError**: Capturado cuando el usuario ingresa caracteres no numéricos en una operación que requiere enteros.
* **ZeroDivisionError**: Gestionado para evitar el error lógico de dividir por cero.

**Lógica Aplicada:**
Se utiliza la cláusula `else` para ejecutar el resultado solo si no hubo errores, y `finally` para mostrar un mensaje de cierre independientemente del resultado de la operación.

### Parte B: Acceso a Estructuras de Datos (excepciones_B.py)

Este script se enfoca en la validación de índices y tipos de datos al trabajar con listas:

* **IndexError**: Capturado cuando se intenta acceder a una posición fuera del rango definido en la lista de colores.
* **Captura de Mensajes (as e)**: Se implementa la captura del mensaje de error del sistema para una depuración más precisa.

---

## Conceptos Técnicos Implementados

### 1. El Bloque Try-Except
Permite aislar el código propenso a errores y definir rutas de escape específicas para cada tipo de excepción detectada.

### 2. Cláusulas Complementarias
* **else**: Bloque de código que se ejecuta únicamente si el bloque `try` finaliza con éxito.
* **finally**: Bloque de ejecución obligatoria, utilizado comúnmente para liberar recursos o confirmar el fin de un proceso.

---

## Ejemplo de Flujo Lógico

La valid
