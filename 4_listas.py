mi_lista = ["Python", "Django", "React", "Angular"]
# Imprimir la lista
print(mi_lista)

# Acceder a un elemento de la lista
print("Acceder a un elemento de la lista")
print(mi_lista[0]) # Python
print(mi_lista[3]) # Angular

# Acceder al ultimo elemento de la lista
print("Acceder al ultimo elemento de la lista")
# cuando ingreso un numero negativo comienza en sentido contrario
print(mi_lista[-1])
print(mi_lista[-4]) # python

# Modificar un elemento de la lista
print(mi_lista)
mi_lista[1] = "Java"
print(mi_lista)

# Añadir un elemento a la lista
mi_lista.append("Vue")
print(mi_lista)

# Añadir un elemento al comienzo de la lista
print("Añadir un elemento al comienzo de la lista")
print(mi_lista)
mi_lista.insert(0, "C#") # al comienzo de la lista
print(mi_lista)
mi_lista.insert(2, "Flutter")
print(mi_lista)
mi_lista.insert(4, "Android")
print(mi_lista)

# Longitud
print(len(mi_lista))