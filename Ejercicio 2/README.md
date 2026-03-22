# Ejercicio 2: Sistema de Gestión de Cuenta Bancaria 

Este proyecto implementa una clase en Python para simular el comportamiento de una cuenta bancaria, reforzando conceptos de **encapsulamiento** y **lógica de métodos** dentro del paradigma de Programación Orientada a Objetos (POO).

---

## 📝 Descripción del Código

El archivo contiene la clase `CuentaBancaria`, la cual permite gestionar el flujo de dinero (depósitos y retiros) validando siempre la disponibilidad de fondos.

### Atributos:
* **`titular`**: Nombre del dueño de la cuenta.
* **`numeroCuenta`**: Identificador único de la cuenta.
* **`saldo`**: Monto de dinero disponible (convertido a `float` para precisión decimal).

### Funcionalidades (Métodos):
1.  **`depositar(cantidad)`**: Suma el monto especificado al saldo actual.
2.  **`retirar(cantidad)`**: Resta el monto especificado, pero solo si hay fondos suficientes. Incluye un mensaje de error si la operación no es posible.
3.  **`consultarSaldo()`**: Retorna el saldo actual de la cuenta.
4.  **`mostrarInformacion()`**: Presenta de forma legible los datos del titular y su saldo.

---

## 🔢 Lógica de Validación

Para el método de retiro, se aplica una estructura condicional que garantiza la integridad de la cuenta:

$$\text{Si } (\text{cantidad} \leq \text{saldo}) \rightarrow \text{Aprobar Retiro}$$
$$\text{Si } (\text{cantidad} > \text{saldo}) \rightarrow \text{Error: Fondos Insuficientes}$$

---

## 🚀 Ejemplo de Ejecución

En el script se crearon tres instancias iniciales:
* **Mily**: Cuenta con saldo inicial de $1000.0.
* **Lynn**: Cuenta con saldo inicial de $500.0.
* **Pedro**: Cuenta con saldo inicial de $0.0.

### Flujo de prueba:
1. Se depositan **$500**.
2. Se retiran **$200** (Exitoso).
3. Se intenta retirar **$2000** (Error esperado por fondos insuficientes).

---
**Mily L.M.** | *Ingeniería en Sistemas Computacionales - ITE*
