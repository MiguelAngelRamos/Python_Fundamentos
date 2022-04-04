from automovil import Automovil

class AutoDeportivo(Automovil):
  cv = 120
  def __init__(self, marca, color, cv):
    self.marca = marca
    self.color = color
    self.cv = cv
    
    
auto_deportivo = AutoDeportivo("Mazda MX-5","Negro", 250)
print(f'Marca: {auto_deportivo.marca}, Color: {auto_deportivo.color}, CV: {auto_deportivo.cv}')