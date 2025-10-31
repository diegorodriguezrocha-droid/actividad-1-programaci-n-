print(=*22 )
print("ejercicio 1\n")

edad = int(16)

if edad >= 16:
    print(" puedes jugar \n")
    else:
        print(" no puedes jugar \n")


    print("="*18)
print("ejercicio 2\n")

calificacion = int(input(" ingresa tu calificacion (0 a 100): "))

if calificacion >= 90:
    print("Excelente\n")
    elif calificacion >= 70:
        print("Aprobado\n")
        else:
            print("Reprobado\n")


print("="*22)
print("ejercicio 3\n")
 
edad = int(input(" ingresa tu edad: "))
genero = input(" ingresa tu genero favorito (accion, comedia, terror): ").lower()

if edad < 13:
    if genero == "accion":
        print("Te recomendamos ver: Spider-man (PG-13)\n")
    elif genero == "comedia":
        print("Te recomendamos ver: Shrek (PG-13)\n")
    elif genero == "terror":
        print("Te recomendamos ver: Scary Stories (PG-13)\n")
    else:
        print("Genero no reconocido\n")

elif edad <= 18 
if genero == "accion":
        print("Te recomendamos ver: John Wick\n")
elif genero == "comedia":
        print("Te recomendamos ver: Superbad\n")
elif genero == "terror":
        print("Te recomendamos ver: The Conjuring\n")
        else:
            print("Genero no reconocido\n")
