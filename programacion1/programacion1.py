#1. Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2.Crear un programa que pida al usuario su nombre e imprima por pantalla 
# un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa 
# “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas 
# print(f…) para

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar 
# de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en 
# Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

nombre2 = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")
 
#4. Crear un programa que pida al usuario el radio de un círculo e imprima por 
# pantalla su área y su perímetro.

import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

#5. Crear un programa que pida al usuario una cantidad de segundos e imprima 
# por pantalla a cuántas horas equivale

segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

#6. Crear un programa que pida al usuario un número e imprima por pantalla la tabla 
# de multiplicar de dicho número

numero = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#7. Crear un programa que pida al usuario dos números enteros distintos del 0 y 
# muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y 
# restarlos.

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

#8. Crear un programa que pida al usuario su altura y su peso e imprima por pantalla 
# su índice de masa corporal. Tener en cuenta que el índice de masa corporal se 
# calcula del siguiente
#modo:   𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#             (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#9. Crear un programa que pida al usuario una temperatura en grados Celsius e imprima 
# por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente 
# equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =  9 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
#                            5

celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")

#10. Crear un programa que pida al usuario 3 números e imprima por pantalla el 
# promedio de dichos números.

numProm1 = float(input("Ingresa el primer número: "))
numProm2 = float(input("Ingresa el segundo número: "))
numProm3 = float(input("Ingresa el tercer número: "))
promedio = (numProm1 + numProm2 + numProm3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")







