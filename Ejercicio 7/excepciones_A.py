### Ejercicio 7: Manejo de Excepciones

print("="*50)
print("PARTE 1: División con manejo de errores")
print("="*50)

try:
    a = int(input("Ingresa el numerador: "))
    b = int(input("Ingresa el denominador: "))
    total = a / b
    


except ValueError:
    print("Error: Debes ingresar un número entero, no otros símbolos.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else:
    print(f"El resultado de {a} dividido por {b} es: {total}")

finally:
    print("¡Gracias por usar el programa de división!")