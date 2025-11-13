# paso 1: Crear las dos matrices
matriz_a = [
    (1,2),
    (3,4)
]
matriz_b = [
    (5,6),
    (7,8)
]
# paso2: Crear matriz vacia para el resultado 
resultado = ()
# paso 3: Recorrer las matrices y sumar 
for i in range(2): # 2 filas
    fila =() # Crear fiola vacia 

    for j in range(2): # 2 columnas
        suma = matriz_a[i][j] + matriz_b[i][j]
        fila.append(suma9) # Agregar a la fila

        resultado.append(fila) # Agregar fila al resultado 

        # paso4: Mostrar resultado
        print("Mtriz A:")
for fila in matriz_a:
    for elemento in fila:
        print(elemento, end=" ")
        print() 

        print("\nResultado A + B:")
        for fila in resultado:
            for elemento in fila:
                print(elemento, end=" ")
            print()

            