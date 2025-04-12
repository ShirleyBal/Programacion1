#  1.	Verificar si es mayor de edad
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#  2.	Verificar las notas
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#  3.	Verificar si el número ingresado es par
numeroo = int(input("Ingrese un número: "))

if numeroo % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4.	Verificar categorias de edad
edadCat = int(input("Ingrese su edad: "))

if edadCat < 12:
    print("Usted es un/a niño/a")
elif edadCat >= 12 and edadCat < 18:
    print("Usted es un/a adolescente")
elif edadCat >= 18 and edadCat < 30:
    print("Usted es un/a adulto/a joven")
else:
    print("Usted es un/a adulto/a")

# 5.	Verificar contraseña con 8 a 14 caracteres
contraseña = input("Ingrese su contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#  6.  Generar la lista de 50 números aleatorios entre 1 y 100
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)
moda_valor = mode(numeros_aleatorios)

# # Mostrar los valores calculados
print("Lista de números:", numeros_aleatorios)
print("Media:", media_valor)
print("Mediana:", mediana_valor)
print("Moda:", moda_valor)

#  Determinar el tipo de sesgo
if media_valor > mediana_valor > moda_valor:
    print("Distribución con sesgo positivo (a la derecha)")
elif media_valor < mediana_valor < moda_valor:
    print("Distribución con sesgo negativo (a la izquierda)")
elif media_valor == mediana_valor == moda_valor:
    print("Distribución sin sesgo")
else:
    print("Distribución no claramente sesgada")

# 7. String terminado en vocal
stringIngresado = input("Ingrese una palabra: ")
ultima_letra = stringIngresado[-1]
vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

if ultima_letra in vocales: # Verificamos si la última letra es una vocal
    print(stringIngresado + "!")
else:
    print(stringIngresado)

print("Última letra:", ultima_letra)

# 8. Mayusculas y minusculas
nombreIngr = input("Ingrese su nombre: ")
opcionIng = input("Ingrese si quiere mayúscula, minúscula o solo la primera letra en mayúscula (1, 2 o 3): ")
resultadoNom = ""

if opcionIng == '1':
    resultadoNom = nombreIngr.upper()
elif opcionIng == '2':
    resultadoNom = nombreIngr.lower()
elif opcionIng == '3':
    resultadoNom = nombreIngr.title()
else:
    resultadoNom = "Opción inválida"

print("Resultado:", resultadoNom)

# 9. Magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

# 10. Estacion y ubicación
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1 a 12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio not in ("N", "S") or not (1 <= mes <= 12) or not (1 <= dia <= 31):# Verificar si la entrada es válida
    print("Entrada inválida.")
else:
    
    fecha = (mes, dia) # Convertimos mes y día en un número para comparar fechas más fácilmente

    if hemisferio == "N": # Definir estaciones para el hemisferio norte
        if (fecha >= (12, 21) and fecha <= (12, 31)) or (fecha >= (1, 1) and fecha <= (3, 20)):
            estacion = "Invierno"
        elif fecha >= (3, 21) and fecha <= (6, 20):
            estacion = "Primavera"
        elif fecha >= (6, 21) and fecha <= (9, 20):
            estacion = "Verano"
        elif fecha >= (9, 21) and fecha <= (12, 20):
            estacion = "Otoño"
    
    elif hemisferio == "S": # Definir estaciones para el hemisferio sur
        if (fecha >= (12, 21) and fecha <= (12, 31)) or (fecha >= (1, 1) and fecha <= (3, 20)):
            estacion = "Verano"
        elif fecha >= (3, 21) and fecha <= (6, 20):
            estacion = "Otoño"
        elif fecha >= (6, 21) and fecha <= (9, 20):
            estacion = "Invierno"
        elif fecha >= (9, 21) and fecha <= (12, 20):
            estacion = "Primavera"

    print("Estás en", estacion)


