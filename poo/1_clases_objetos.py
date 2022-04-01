class Automovil:
  marca = ""
  color = "blanco"  # color por defecto
  def __init__(self, marca, color):
    self.marca = marca
    self.color = color

# Creando una instancia de la clase Automovil

auto1 = Automovil("Hyundai", "Rojo") # creando un objeto

# Imprimir
print(auto1.color)
print(auto1.marca)
print(f'Marca: {auto1.marca}, color: {auto1.color}')

    