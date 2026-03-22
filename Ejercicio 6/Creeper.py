from Mob import Mob

class Creeper(Mob):
    """Mob agresivo, suena '...Ssssss', corre hacia el jugador."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    def hacer_sonido(self) -> str:
        return "...Ssssss"     
       
    def comportamiento(self) -> str:
        return "lento pero agresivo"

    def moverse(self) -> str:
        return "Corre directamente hacia el jugador"