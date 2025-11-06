print("Ejercicio 1 con while")

# Inicializamos una variable contador
contador_numero = 1 

# Mientras contador sea menor o igual a 5
while contador_numero <= 5:
    print(f"numero: {contador_numero}")
    contador_numero = contador_numero + 1  # Incrementamos el contador



print("Ejercicio 2 con while - cuenta regresiva")
# Inicializamos el contador en 5
numero = 5

# Mientras numero sea mayor que 0
while numero > 0:
    print(f"faltan: {numero} segundos...")
    numero = numero - 1  # Decrementamos el contador

    print("Despegue!")


print("Ejercicio 3 con while - suma acumulativa")
# Inicializamos las variables
numero = 1 
suma = 0

# Mientras numero sea menor o igual a 50
while numero <= 50:
    suma = suma + numero  # Acumulamos la suma
    numero = numero + 1   # Incrementamos el contador

    print(f" La suma del 1 al 50 es: {suma}\n")


print("\nEjercicio 4 con while - tabla de multiplicar")
# Inicializamos el contador
multiplicador = 1

# Mientras el contador sea menor o igual a 10
while multiplicador <= 10:
    resultado = 7 * multiplicador  
    print(f"7 x {multiplicador} = {resultado}")
    multiplicador = multiplicador + 1 

    print("¡Tabla de multiplicar completa! \n")
    
    
    print("Ejercicio 5 con while - números pares del 2 al 50")
    
    # Inicializamos el contado en 2 (primer número par)
    numeros_pares = 2 

    # Mientras el numero sea menor o igual a 50
    while numeros_pares <= 50:
        print(f"Número par: {numeros_pares}")
        numeros_pares = numeros_pares + 2  # Incrementamos de 2 en 2

        print("¡Todos los pares mostrados!\n")


print("\Ejercicio 6 con while - Dividir un numero a la mitad")
# Inicializamos con un numero 
numero_a_dividir = 100

# Mientras el numero sea mayor o igual a 1
while numero_a_dividir >= 1:
    print(f"Número actual: {numero_a_dividir}")
    numero_a_dividir = numero_a_dividir / 2  # Dividimos entre 2

    print(f"Numero final (menor a 1): {numero_a_dividir}")

    
    print("\nEjercicio 8 - Loop corregido")
# Queremos contar del 1 al 5
contador = 1

while contador <= 5:
    print(f"Numero: {contador}")
    contador = contador + 1  #¡Ahora si incrementaremos!

    print("¡Loop terminado correctamente!\n")
    
