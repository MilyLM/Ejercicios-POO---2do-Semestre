from Mob import Mob

class Enderman(Mob):
    """Mob neutral, sonido distorsionado, se teletransporta."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    def hacer_sonido(self) -> str:  
        return "Sonido distorsionado"    
        
    def comportamiento(self) -> str:
        return "neutral"

    def moverse(self) -> str:
        return "se teletransporta"