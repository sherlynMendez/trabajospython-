nombre= input("introduce tu primer nombre")
if len(nombre)< 5:
    apellido = input("introduce tu apellido")
    nombre = nombre+apellido
    print(nombre.upper())
else:
    print(nombre.lower())