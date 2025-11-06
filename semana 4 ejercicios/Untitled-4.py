print("\nEjercicio 1\n")
canciones = ("As It Was", "Flowers", "Vampire", "Cruel Summwe", "Calm Down")

print("Mis canciones favoritas:")
print(canciones[0])
print(canciones[1])
print(canciones[2])
print(canciones[3])
print(canciones[4])

print("\nEjercicio 2\n")
amigos = ()

print("Lista inicial:", amigos)

amigos.append("Andre")
print("Despues de agregar a Andre:", amigos)

amigos.append("Meli")
print("Despues de agregar a Meli:", amigos)

amigos.append("Xime")
print("Despues de agregar a Xime:", amigos)

print(f"\nTotal de amigos: {len(amigos)}")

print("\nEjercicio 3\n")
calificaciones  = (98, 90, 88, 92, 89)

# Mostrar todas las calificaciones 
print("Tus calificaciones:", calificaciones)

# Calcular el promedio 
suma =sum(calificaciones)
promedio = suma / len(calificaciones)
print(f"Promedio: {promedio}")

# Encontrar la mejor y peor calificaciones 
mejor = max(calificaciones)
peor = min(calificaciones)
print(f"Mejor calificación: {mejor}")
print(f"Peor calificación: {peor}")

print("\nEjercicio 4\n")
carrito = []
# Agregar productos
print("Agregando productos al carrito...")
carrito.append("iphone15")
carrito.append("Airpods")
carrito.append("Funda")
carrito.append("Cargador")

print(Carrito actual:", carrito)
print(f"Productos en el carrito: {len(carrito)}")

#Decidiste que no quieres la funda 
print("\nEliminando la funda del carrito...")
carrito.remove("Funda")

print("Crrito final:", carrito)
print(f"Total de productos: {len(carrito)}

print("\nEjercicio 5\n")

Videojuegos = ("Minecraft", "Fornite", "Valorant", "Roblox") "GTA V")

print("MI TOP 5 DE VIDEOJUEGOS:)
print(videojuegos)

#Mostrar el primero y el ultimo 
print(f"\nMi favorito (posición 0): {videojuegos[0]}")
print(f" El de la posicion 5 (ultimo): {videojuegos[-1]}")

# Cambiar mi juego favorito 
print("\n Cambio de opinion...")
videojuego(0) = "Apex Legends"

print(Top 5 actualizado:")
print(videojuegos)

print("\nEjercicio 6\n")
series = ["Stranger Things", "Wednesday", "The Last of us")

print("series para ver:", series)

# Agregar una nueva serie
series.append("One piece")
print("Agregaste 'One Piece':", series)

# Verificar si una serie esta en tu lista
if "Wednesday" in series:
    print("si tienes 'Wednesday' en tu lista.")

if "Breaking Bad"  in series:
    print("No tienes 'Breaking Bad' en tu lista.")

    # ya viste la primera serie, la eliminas
    print(f"\n¡Terminaste de ver {series[0]}!
    series.pop(0)
    print("Series restantes:", series)"))