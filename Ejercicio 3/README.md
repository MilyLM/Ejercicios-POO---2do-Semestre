# Ejercicio: Simulador de Cuidado de Mascota 

Este proyecto implementa una clase en Python que simula el estado de ánimo de una mascota virtual. A través de este ejercicio, se practican conceptos de **encapsulamiento**, **lógica condicional** y la gestión de **estados internos** de un objeto.

---

## 📝 Descripción del Código

La clase `Mascota` permite crear compañeros virtuales con atributos específicos y realizar acciones que afectan su bienestar general.

### Atributos:
* **`nombre`**: El nombre de la mascota.
* **`tipo`**: Especie de la mascota (Perro, Gato, etc.).
* **`edad`**: Edad cronológica.
* **`nivelFelicidad`**: Un valor numérico que representa el ánimo de la mascota (rango 0-100).

### Funcionalidades (Métodos):
1.  **`alimentar()`**: Incrementa la felicidad en **+10** puntos.
2.  **`jugar()`**: Incrementa la felicidad en **+20** puntos.
3.  **`mostrarEstado()`**: Retorna un resumen del nombre, tipo y nivel de felicidad actual.
4.  **`esFeliz()`**: Evalúa si la mascota está de buen humor basándose en un umbral.

---

## Lógica de Negocio y Reglas

El código implementa dos reglas lógicas importantes para mantener la integridad del "simulador":

### 1. Límite de Felicidad (Capping)
Para evitar que la felicidad crezca indefinidamente, se aplica un límite máximo de 100 puntos en los métodos de interacción:

$$nivelFelicidad = \min(100, nivelFelicidad + \text{incremento})$$

### 2. Condición de Bienestar
Se define que una mascota "es feliz" solo si su nivel supera el umbral de 70:

$$Estado = \begin{cases} \text{Feliz} & \text{si } nivelFelicidad > 70 \\ \text{Triste/Neutral} & \text{si } nivelFelicidad \leq 70 \end{cases}$$

---

##  Ejemplo de Uso

En el script se prueban dos casos iniciales:
* **Firulais (Perro)**: Comienza con 50 de felicidad (No es feliz inicialmente).
* **Michi (Gato)**: Comienza con 90 de felicidad (Es feliz inicialmente).

Tras interactuar con **Firulais** (alimentar + jugar), su felicidad sube a 80, cambiando su estado a "Feliz".

---
**Mily L.M.** | *Programación Orientada a Objetos - ITE*
