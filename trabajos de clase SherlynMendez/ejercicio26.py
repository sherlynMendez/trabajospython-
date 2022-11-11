palabra = input("porfavor introduce una palabra")
primera= palbra[0]
longitud = len(palabra)
resto= palabra [1: longitud]
if primera != "a" and first != "e" and first != "o" and first != "u":
    palabranueva = resto + primera + "ay"
else:
    palabranueva = palabra + "way"
print(palabranueva.lower())