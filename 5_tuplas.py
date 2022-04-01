# Las tuplas son inmutables

mi_tupla = ("Python", "Django", "React", "Vue")
print(mi_tupla)

# acceder a un elemento 
print(mi_tupla[0]) # EL primer elemento
print(mi_tupla[-1]) # EL ultimo elemento

# Intenemos modificar un elemento de la tupla
mi_tupla[2] = "Angular"
print(mi_tupla)