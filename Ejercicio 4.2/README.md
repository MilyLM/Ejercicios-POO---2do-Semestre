# Ejercicio 4.2: La Taberna de los Aventureros 

Este proyecto simula un sistema de registro para una taberna de fantasía, utilizando los conceptos pilares de la **Programación Orientada a Objetos (POO)**: **Herencia** y **Sobrescritura de Métodos** (Polimorfismo).

---

## 📝 Descripción del Proyecto

El sistema permite gestionar diferentes tipos de aventureros que comparten características base pero poseen habilidades únicas según su clase profesional.

### Estructura de Clases (Jerarquía)


1.  **Clase Base (`Aventurero`)**: Define los atributos comunes (`nombre`, `nivel`) y los métodos generales (`presentarse`).
2.  **Clases Hijas (Especializaciones)**:
    * **Guerrero**: Especialista en combate cuerpo a cuerpo, añade el atributo `arma`.
    * **Mago**: Maestro de las artes arcanas, añade el atributo `hechizo`.
    * **Arquero**: Combatiente a distancia, añade el atributo `flechas` y gestiona el consumo de munición.

---

## 🛠️ Conceptos Aplicados

### 1. Herencia
Todas las clases hijas heredan de `Aventurero`, permitiendo la reutilización de código y una estructura organizada.

### 2. Sobrescritura de Métodos (Overriding)
Cada clase hija redefine el método `usar_habilidad()` para mostrar un comportamiento específico:
* **Guerrero**: Ataca con su arma.
* **Mago**: Lanza un hechizo.
* **Arquero**: Dispara flechas y disminuye su contador interno:
    $$flechas_{final} = flechas_{inicial} - 1$$

---

## 📂 Estructura de Archivos

* `Aventurero.py`: Clase padre.
* `Guerrero.py`: Subclase de Guerrero.
* `Mago.py`: Subclase de Mago.
* `Arquero.py`: Subclase de Arquero.
* `main.py`: Script principal que instancia a los héroes y ejecuta sus acciones.

---

## Ejemplo de Salida

Al ejecutar el `main.py`, el sistema genera una interacción como la siguiente:

```text
Soy Thorin, aventurero de nivel 8
Thorin ataca con su Hacha! ⚔️
---
Soy Gandalf, aventurero de nivel 15
Gandalf lanza Bola de fuego! 
---
Soy Legolas, aventurero de nivel 10
Legolas dispara una flecha! Le quedan 29. 🏹
