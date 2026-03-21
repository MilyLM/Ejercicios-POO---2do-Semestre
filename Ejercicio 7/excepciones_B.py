###
## Excepciones básicas | Capturar múltipples excepciones

#Parte 2

print("="*50)
print("Acceso a una lista")
print("="*50)   

#Creamos una lista de colores
colores = ["rojo", "verde", "azul", "amarillo"]
print(f"lista de colores: {colores} (indices 0,1,2,3)")

try:
    indice = int(input("Qué color qiueres acceder? (ingresa un número del 0 al 3): "))
    print(f"El color seleccionado es: {colores[indice]}")

except ValueError as e:
    print(f"❌ ValueError: {e}")
except IndexError as e:
    print(f"❌ IndexError: {e}")
    print(f"Recuerda que los índices válidos son del 0 al 3")

finally:
    print("-- Fin del programa --")

