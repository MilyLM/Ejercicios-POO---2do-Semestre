# Ejercicio 4: Sistema de Menú de Restaurante 

Este proyecto simula la gestión de un menú digital para un restaurante. Se aplica el concepto de **Herencia en Python** para organizar diferentes tipos de productos (comida, bebidas y postres) bajo una estructura lógica y eficiente.

---

## Descripción del Proyecto

El sistema permite categorizar los elementos del menú compartiendo atributos básicos pero manteniendo sus características únicas.

### Jerarquía de Clases

* **Clase Base (`Platillo`)**: Contiene los datos generales de cualquier producto del menú.
    * **Atributos**: `nombre`, `precio`.
    * **Métodos**: `mostrar_info()`, `tipo()`.

* **Clases Hijas**:
    * **`Comida`**: Añade el atributo `categoria` (Entrada, Principal, etc.).
    * **`Bebida`**: Añade el atributo `temperatura` (Fría, Caliente).
    * **`Postre`**: Añade el atributo `es_sin_gluten` (Booleano).

---

##  Conceptos Técnicos Clave

### 1. Uso de `super().__init__()`
Para que las clases hijas puedan heredar correctamente el nombre y el precio, se utiliza la función `super()`. Esto permite llamar al constructor de la clase padre y luego añadir los atributos específicos:

```python
def __init__(self, nombre, precio, atributo_especifico):
    super().__init__(nombre, precio)
    self.atributo_especifico = atributo_especifico
