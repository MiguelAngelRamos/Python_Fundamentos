class Automovil:
  marca = ""
  color = ""
  encendido = False
  velocidad = 0
  
  def __init__(self, marca, color):
    self.marca = marca
    self.color = color
    
  def encender(self):
    self.encendido = True
    
  # acelerar
  def set_velocidad(self, velocidad):
    self.velocidad = velocidad

auto1 = Automovil("Hyundai", "Rojo")
# auto2 = Automovil("Ford", "Negro")

# Encender automovil
auto1.encender()
auto1.set_velocidad(60)

if auto1.encendido:
  print(f'El Automovil esta encendido y va a una velocidad de {auto1.velocidad} km/h')
else:
  print('EL automovil esta apagado')