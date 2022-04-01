tabla = int(input('¿Que tabla deseas calcular?'))
numeros = range(0, 11)

for num in numeros:
  print(f'{tabla} x {num} = {tabla * num}')