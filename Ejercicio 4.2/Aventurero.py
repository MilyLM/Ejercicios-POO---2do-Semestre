class Aventurero:
    def __init__(self,nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un aventurero de nivel {self.nivel}.")

    def usar_habilidad(self):
        print(f"Habilidad desconocida...")
        