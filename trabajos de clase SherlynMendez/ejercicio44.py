num= int(input("a cuantos quieres invitar a la fiesta"))
if num < 10:
    for i in range (0,num):
        name= input("introduce un nombre")
        print(nombre,"ha sido invitado")
else:
    print("demaciada gente")