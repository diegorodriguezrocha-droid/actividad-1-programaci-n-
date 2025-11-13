# Creamos las matrices que vamos a rastrear
matriz_a = [
    (10, 15, 20),
    (25, 30, 35),
    (40, 45, 50)
]
matriz_b = [
    (2, 5, 8),
    (3, 10, 15),
    (5, 20, 25)
]
# Crear una matriz vacia para guardar el resultado 
resultado = ()
#Recorre las matriculas y restar elementos por elemento
for i in range (3): # 3 columnas 
    resta = matriz_a(1)(j) - matriz_b(i)(j) # Resta elementos 
    fila.append(resta) # Agregar resultado a la fila
    resultado.append(fila) # Afrefar fila completo al resultado 

#Mostramos las matrices y el resultado 
print("Matriz A:")
for fila in matriz_a:
    for elemento in fila:
        print(f"{elemento:3}", end=" ") # :3 alinea los numeros 
        print()

print("Matriz B:")
for fila in matriz_b:
    for elemento in fila:
        print(f"{elemento:3}", end=" ")
        print()
        print("\nResultado (A - B):")
        for fila in resultado:
            for elemento in fila:
                print(f"{elemento:3}", end=" ")
            print()
            