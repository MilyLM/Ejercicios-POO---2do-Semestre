from Aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, nivel, hechizo):
        self.nombre = nombre
        self.nivel = nivel
        self.hechizo = hechizo
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un mago de nivel {self.nivel}.")
    def usar_habilidad(self):
        print(f"{self.nombre} lanza el hechizo {self.hechizo}! 🔮")