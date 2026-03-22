# Ejercicio 5: Abstracción en Python 

En este ejercicio se explora el concepto de **Abstracción**, uno de los pilares de la Programación Orientada a Objetos. Se utiliza para definir clases "plantilla" que no pueden ser instanciadas directamente, sino que sirven como base para otras clases.

---

##  Descripción del Código

El archivo `abstraccion.py` utiliza el módulo estándar de Python **`abc`** (Abstract Base Classes) para definir una estructura jerárquica obligatoria.

### Componentes Principales:
* **Clase Abstracta (`Animal`)**: Actúa como una interfaz o plano general. Al heredar de `ABC`, le indicamos a Python que esta clase no es un objeto final, sino un modelo.
* **Método Abstracto (`hablar`)**: Marcado con el decorador `@abstractmethod`. Este método no tiene implementación en la clase padre (solo un `pass`), obligando a cualquier clase hija a definir su propia versión.

---

## Funcionamiento Técnico

### Las Clases Concretas
Para que un "Animal" pueda existir en el programa, debe especializarse:
1.  **`Perro`**: Implementa `hablar()` retornando `"Guau!"`.
2.  **`Gato`**: Implementa `hablar()` retornando `"Miau!"`.

> **Regla de Oro:** Si una clase hereda de una clase abstracta y no implementa todos los métodos marcados como `@abstractmethod`, Python lanzará un error y no permitirá crear el objeto.

---

## 📂 Lógica de Implementación

El flujo del programa sigue esta estructura de herencia:

1. **Definición**: Se importa `ABC` y `abstractmethod`.
2. **Contrato**: La clase `Animal` establece que todo animal *debe* hablar.
3. **Ejecución**: Se crean las instancias y se llaman a los métodos específicos de cada especie.

---

##  Ejemplo de Salida

```text
Guau!
Miau!
