class Mascota:
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad
    
    def alimentar(self):
        self.nivelFelicidad += 10
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100
        print(f"Has alimentado a {self.nombre} +10 puntos")

    def jugar(self):
        self.nivelFelicidad += 20
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100
        print(f"Has jugado con {self.nombre} +20 puntos")


    def mostrarEstado(self):
        return f"{self.nombre} es un {self.tipo} con felicidad: {self.nivelFelicidad}"


    def esFeliz(self):
        return self.nivelFelicidad > 70

mascota1 = Mascota("Firulais", "Perro", 3, 50)
mascota2 = Mascota("Michi", "Gato", 2, 90)


print(mascota1.mostrarEstado())
print(f"¿Es feliz? {mascota1.esFeliz()}")

mascota1.alimentar()
mascota1.jugar()

print(mascota1.mostrarEstado())
print(f"¿Es feliz ahora? {mascota1.esFeliz()}")

print(f"\nEstado inicial de {mascota2.nombre}: {mascota2.nivelFelicidad}")
mascota2.alimentar() 
print(mascota2.mostrarEstado())