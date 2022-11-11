import math
radio= int(input("introduce el radio del circulo"))
profundidad = int(input("introduce la profundidad"))
area= math.pi*(radio*2)
volumen= area*profundidad
print(round(volumen,3))