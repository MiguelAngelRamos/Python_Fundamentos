class Automovil:
  marca = ""
  color = ""
  __encendido = False # __ hacemos private esta propiedad
  velocidad = 0
  
  def __init__(self, marca, color):
    self.marca = marca
    self.color = color
    
  def set_encender(self):
    self.__encendido = True
    
  # acelerar
  def set_velocidad(self, velocidad):
    self.velocidad = velocidad
    
  def get_encendido(self):
    return self.__encendido