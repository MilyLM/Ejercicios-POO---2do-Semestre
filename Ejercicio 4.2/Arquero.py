from Aventurero import Aventurero

class Arquero():
    def __init__(self, nombre, nivel, flecha): 
     
        self.nombre = nombre
        self.nivel = nivel
        self.flecha = flecha
    
       

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un arquero de nivel {self.nivel}.")

    def usar_habilidad(self):
        self.flecha -= 3
        print(f"{self.nombre} dispara tres Flechas! 🏹. Le quedan: {self.flecha}")
    