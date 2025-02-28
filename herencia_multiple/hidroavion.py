from navegable import Navegable
from volador import Volador

class Hidroavion(Navegable, Volador):
  def navegar(self):
    return "El hidroavión está navegando."
  
  def volar(self):
      return "El hidroavión está volando."
