# Ejercicio 1: Modelado de Clase Estudiante

Este ejercicio consiste en la creación de una clase base en Python para gestionar la información de un estudiante, aplicando conceptos fundamentales de la **Programación Orientada a Objetos (POO)** como el método constructor, atributos de instancia y métodos de comportamiento.

---

## 📝 Descripción del Código

El archivo `Estudiante (1).py` define una clase que permite almacenar datos personales y académicos, además de realizar operaciones básicas con las calificaciones.

### Atributos:
* **`nombre`**: Nombre del estudiante (String).
* **`edad`**: Edad del estudiante (Integer).
* **`carrera`**: Carrera que cursa (String).
* **`calificaciones`**: Una lista dinámica para almacenar notas (List).

### Métodos principales:
1.  **`__init__`**: Inicializa los atributos básicos y prepara la lista de calificaciones vacía.
2.  **`setCalificaciones`**: Permite agregar nuevas notas a la lista mediante el método `.append()`.
3.  **`getNombre`**: Retorna el nombre almacenado en el objeto.
4.  **`mostrarPromedio`**: Realiza el cálculo del promedio académico.
5.  **`mostrarInformacionUsuario`**: Retorna un *f-string* con una presentación formal del estudiante.

---

## 🔢 Lógica Matemática
Para el cálculo del promedio, el código suma todas las calificaciones y las divide entre el total de elementos:

$$\text{Promedio} = \frac{\sum_{i=1}^{n} x_i}{n}$$

*Nota: El código incluye una validación para retornar 0 si la lista está vacía, evitando errores de división por cero.*
