persona = {'name': 'Miguel', 'last_name': 'Ramos'}
print(persona)
# Acceder al contenido de una key del diccionario
print(persona['name'])
print(f'Mi nombre es: { persona["name"]}')

# Añadir una nueva propiedad al diccionario
print(persona)
persona['city'] = 'Santiago'
print(persona)

# Eliminar una propiedad
del persona['last_name']
print(persona)

# Podemos observar la longitud que tiene el diccionario
print(len(persona))