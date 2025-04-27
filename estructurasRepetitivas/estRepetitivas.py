#Trabajo Practico: Estructuras Repetitivas:

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero_usuario = int(input("Ingrese un número para determinar cuántos dígitos tiene: "))
numero_absoluto = abs(numero_usuario) # Convertimos el número a positivo por si es negativo
cant_digitos = len(str(numero_absoluto)) # Convertimos a string y contamos los caracteres

print(f"El número tiene {cant_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

primer_Num = int(input("Ingrese un número: "))
segundo_Num = int(input("Ingrese otro número para sumar los numeros intermedios: "))
total = 0

for i in range(primer_Num + 1, segundo_Num): #para no incluirlos
    total +=i

print("El numero total es ", total)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total_Suma = 0

while True:
    num_usuario = int(input("Ingrese un número (0 para terminar): "))
    if num_usuario == 0:
        break
    total_Suma += num_usuario

print("La suma total es:", total_Suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

num_ingresado = int(input("Ingresa un número entre 0 y 9 para adivinar: "))

while num_ingresado != numero_aleatorio:
    intentos += 1
    print("Incorrecto. Intenta de nuevo.")
    num_ingresado = int(input("Ingresa un número entre 0 y 9 para adivinar: "))

intentos += 1  # Contamos el intento correcto
# print(f"¡Acertaste! Te tomó {intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

for i in range(100, -1, -1):
    if i % 2 == 0: #si quiero agregar if aunque no es necesario
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num_ingres = int(input("Ingresa un número: "))
suma_total = 0

for i in range(0, num_ingres+1):
    suma_total +=i
    
print("La suma total es ", suma_total)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0

for _ in range(100):  # Puedes cambiar 100 por otro número para probar
    num_ingresado = int(input("Ingresa un número entero: "))
    
    if num_ingresado % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

    if num_ingresado > 0:
        num_positivos += 1
    elif num_ingresado < 0:
        num_negativos += 1

print("\nResultados:")
print(f"Números pares: {num_pares}")
print(f"Números impares: {num_impares}")
print(f"Números positivos: {num_positivos}")
print(f"Números negativos: {num_negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 100  # Puedes cambiarlo a un número menor para probar
suma_totalE = 0

for _ in range(cantidad_numeros):
    num = int(input("Ingrese un número entero: "))
    suma_totalE += num

media = suma_totalE / cantidad_numeros

print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número para invertir sus dígitos: ")

numero_invertido = numero[::-1]

print(f"El número invertido es: {numero_invertido}")