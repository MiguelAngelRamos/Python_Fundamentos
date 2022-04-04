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
  
# HERENCIA
class AutoDeportivo(Automovil):
  cv = 120
  def __init__(self, marca, color, cv):
    self.marca = marca
    self.color = color
    self.cv = cv
    
auto_deportivo = AutoDeportivo("Mazda MX-5","Negro", 250)
print(f'Marca: {auto_deportivo.marca}, Color: {auto_deportivo.color}, CV: {auto_deportivo.cv}')