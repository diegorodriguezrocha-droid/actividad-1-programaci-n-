print("\nEjemplo 1 mostrar el menu\n")

def mostrar_menu():
print("=== MENÚ ===")
print("1. Hamburguesa")
print ("2. Pizza")
print ("3. Tacos")

# La usas así y ya no tienes que escribir todo el menu mostrar_menu()

print ("\nE jemplo 2 la fav cancion\n")

def reproducir_favorita():
print ("S Reproduciendo: "Blinding tights" de The Weeknd")

#  usas así:
reproducir_favorita()

print ("InEjemplo 3 reglas del juego\n")

def mostrar_reglas():
print ("REGLAS DEL JUEGO: ")
print("- No hacer trampa")
print("- Respetar turnos")
print("- Divertirse")

# la usas así: 
mostrar_reglas()

#FUNCIONES CON PARAMETROS
print("\nEjemplo 4 \n")

def reproducir cancion (nombre_cancion):
print(f"Reproduciendo: (nombre_cancion)")

#  usas así (cada vez es DIFERENTE):
reproducir_cancion ("Bad Bunny - Titi Me Preguntó")
reproducir_cancion("Karol G - 7Q6")
reproducir_cancion("Taylor Swift - Anti-Hero")

def calcular_impuesto(precio):
total = precio * 1.16 # 16%
return total

# La usas asi (cada precio es DIFERENTE):
print(calcular_impuesto(110))
print (calcular_impuesto(500))
print (lcular_impuesto(1200))

#Ejercicio 6
print("\nEjercicio 3\n")
def calcular_promedio(cal1, cal2, cal3):
    Suma = cal1 + cal2 + cal3
    Promedio = suma / 3
    return promedio
    
    promedio = calcular_promedio(85, 90, 78)
    print(f"Tu promedio es: {promedio}")

    promedio2 = calcular_promedio(100, 95, 88)
    print(f"Tu promedio es:{promedio2}")
