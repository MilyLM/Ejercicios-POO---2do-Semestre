from Aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, nivel, arma):
        self.nombre = nombre
        self.nivel = nivel  
        self.arma = arma
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un guerrero de nivel {self.nivel}.")
    def usar_habilidad(self):
        print(f"{self.nombre} ataca con su {self.arma}! ⚔️")

