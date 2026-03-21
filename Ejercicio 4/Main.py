from Comida import Comida
from Bebida import Bebida
from Postre import Postre

# Crear objetos
taco = Comida("Tacos al pastor", 85.0, "Principal")
torta = Comida("Torta de asada", 85.0, "Principal")

limonada = Bebida("Limonada", 35.0, "Fría")
café = Bebida("Café", 30.0, "Caliente")

flan = Postre("Flan", 45.0, False)
brownie = Postre("Brownie sin gluten", 50.0, True)

# Mostrar información
print(" --- Menú del Restaurante ---")
print()
print("Comidas:")
taco.mostrar_info()
taco.tipo()
print()
torta.mostrar_info()
torta.tipo()
print()
print("Bebidas:")
limonada.mostrar_info()
limonada.tipo()
print()
café.mostrar_info()
café.tipo()
print()
print("Postres:")
flan.mostrar_info()
flan.tipo()
print()
brownie.mostrar_info()
brownie.tipo()