from Arquero import Arquero
from Guerrero import Guerrero
from Mago import Mago
  


guerrero = Guerrero("Thorin", 5, "Espada de Acero")
arquero = Arquero("Legolas", 4, 30)
mago = Mago("Gandalf", 10, "Bola de Fuego")


  
   
  
guerrero.presentarse()
guerrero.usar_habilidad()
print("---")
arquero.presentarse()
arquero.usar_habilidad()
print("---")
mago.presentarse()
mago.usar_habilidad()