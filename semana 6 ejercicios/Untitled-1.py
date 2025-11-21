print("Ejercicio 1\n")

canciones_dia = ("Blinding Lights", "Heat Waves", "Anti-Hero")
canciones_noche =("Levitating", "As It Was")

playlist_completa = canciones_dia + canciones_noche
print(canciones_dia)
print(canciones_noche)
print(playlist_completa)

print("\nEjemplo 2 la fav cancion\n")

def reproducir_favorita():
    print("Reproduciendo: 'Blinding Lights' de The Weeknd")

    # La usas así:
    reproducir_favorita()

    print("\nEjemplo 3 reglas del juego\n")

    def mostrar_reglas():
        print("REGLAS DEL JUEGO:")
        print("- No hacer trampa")
        print("- Respetar turnos")
        print("- Divertirse")

    # La usas así:
    mostrar_reglas()

    # FUNCIONES CON PARAMETROS
    print("\nEjemplo 4\n")

    def reproducir_cancion(nombre_cancion):
        print(f"Reproduciendo: {nombre_cancion}")

    # La usas así (cada vez es DIFERENTE):
    reproducir_cancion("Bad Bunny - Tití Me Preguntó")
    reproducir_cancion("Karol G - TQG")
    reproducir_cancion("Taylor Swift - Anti-Hero")

    def calcular_impuesto(precio):
        total = precio * 1.16 # 16%
        return total

        # La usas así (cada vez es DIFERENTE):
        print(calcular_impuesto(110))
        print(calcular_impuesto(500))
        print(calcular_impuesto(1200))

print("\nEjemplo 5- count\n")

resultados_partidas = ("gane", "perdi", "gane", "gane", "perdi", "gane", "empate")
veces_gane 0 resultados_partidas.count("gane")
print("He ganado:", veces_gane)

print("\nEjemplo 6- index\n")

ranking 0 ("Marcelo", "Mariana", "vane", "abi", "Fer", "Marcelo", "orlando")
mi_posicion 0 ranking.index("mariana2")
print("Estoy en la posicion: ", mi_posicion, "\")

print("\nEjercicio 7 - slicing\n")

juegos = ("Minecraft", "Fornite", "Roblox", "Amoung us", "Valorant", "GTA V", "ACNH", "Call of Duty")
ultimos_tres = juegos(2:5)
print(ultimos_tres)

print("\nEjercicio 8 - recorrer tupla\n")

canciones = ("EYES CLOSED", "The Fate of Ophelia", "When Did You Get Hot?", "Golden")

for cancion in canciones:
    print(cancion)

print("\nEjercicio 9 - Verificar si un elemento existe\n")

grupo_proyecto = ("Meli", "Alex", "Mia", "Andrea")

print("Integrantes del equipo", grupo_proyecto)
print("\n¿Mia esta en el grupo?")
print("Mia" in grupo_proyecto)

print("\n¿Orlando esta en el grupo?")
print("Orlando" in grupo_proyecto)

print("\Ejercicio 10 - Ordenar la tupla\n")

puntuaciones = (580, 250, 1040, 390, 750, 2480, 870, 138, 9389)
puntuaciones_ordenadas = tuple(sorted(puntuaciones))
print(puntuaciones_ordenadas)
