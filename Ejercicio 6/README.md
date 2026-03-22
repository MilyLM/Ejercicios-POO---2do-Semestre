# Ejercicio 6: Abstracción Aplicada - Mobs del Overworld

Este proyecto consiste en el modelado de diferentes criaturas del universo de Minecraft utilizando el concepto de clases abstractas en Python. El objetivo principal es aplicar la abstracción para definir una estructura base que todas las subclases deben implementar obligatoriamente.

---

## Objetivo de Aprendizaje

El propósito de este laboratorio es comprender cómo una clase abstracta actúa como un contrato técnico. Al definir métodos abstractos, se garantiza que cualquier tipo de criatura (Mob) agregada al sistema cuente con comportamientos esenciales de sonido, movimiento y tipo de comportamiento, delegando la implementación específica a cada subclase.

---

## Conceptos Técnicos Implementados

### 1. Clases Abstractas (ABC)
Se utiliza el módulo estándar `abc` de Python para definir la clase `Mob` como una clase base abstracta (Abstract Base Class). Esto impide la instanciación directa de la clase base, asegurando que solo existan objetos de tipos específicos (Vaca, Creeper, etc.).

### 2. Contrato de Métodos (@abstractmethod)
La clase base define tres métodos abstractos que representan el comportamiento obligatorio de cada entidad:
* **hacer_sonido()**: Retorna una cadena con el sonido característico.
* **comportamiento()**: Define la actitud del mob (pasivo, neutral o agresivo).
* **moverse()**: Describe la mecánica de desplazamiento en el entorno.

### 3. Métodos Concretos
El método `presentarse()` es un método concreto heredado por todas las subclases. Este método centraliza la lógica de salida en consola para mostrar los atributos de vida, sonido y movimiento de forma estandarizada, promoviendo la reutilización de código.

---

## Lógica del Contrato

La relación de herencia y la obligación de implementación se rige por la siguiente premisa lógica:

$$\forall \text{ Mob } \in \{\text{Vaca, Creeper, Enderman}\} \implies \exists \text{ Implementación}(\text{sonido, comportamiento, movimiento})$$

Si una subclase omite la implementación de cualquiera de estos métodos, el intérprete de Python generará un error de tipo `TypeError` al momento de intentar crear la instancia.

---

## Estructura de Archivos

El proyecto mantiene una arquitectura modular para facilitar el mantenimiento:
* **Mob.py**: Definición de la clase abstracta base y el contrato técnico.
* **Vaca.py**: Implementación de la entidad de tipo pasivo.
* **Creeper.py**: Implementación de la entidad de tipo agresivo.
* **Enderman.py**: Implementación de la entidad de tipo neutral.
* **main.py**: Script principal que gestiona la colección de objetos y ejecuta las pruebas de sistema.

---

## Ejemplo de Salida

Al ejecutar el programa
