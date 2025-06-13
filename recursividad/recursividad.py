#Aplicación de la Recursividad 

# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try: # Solicitar al usuario un número
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 1:
        print("El número debe ser mayor o igual a 1.")
    else:
        print(f"\nFactoriales del 1 al {numero}:")
        for i in range(1, numero + 1):
            print(f"{i}! = {factorial(i)}")
except ValueError:
    print("Entrada no válida. Debes introducir un número entero.")

# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

# Función recursiva para calcular el número de Fibonacci en la posición n
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try: # Solicitar al usuario una posición
    posicionF = int(input("Introduce una posición entera no negativa: "))
    if posicionF < 0:
        print("La posición debe ser un número entero no negativo.")
    else:
        print(f"\nSerie de Fibonacci hasta la posición {posicionF}:")
        for i in range(posicionF + 1):
            print(f"F({i}) = {fibonacci(i)}")
except ValueError:
    print("Entrada no válida. Debes introducir un número entero.")

# Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general.

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


try: # Algoritmo general para probar la función
    base = float(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente (entero no negativo): "))
    
    if exponente < 0:
        print("El exponente debe ser un número entero no negativo.")
    else:
        resultado = potencia(base, exponente)
        print(f"\n{base}^{exponente} = {resultado}")
except ValueError:
    print("Entrada no válida. Asegúrate de introducir números válidos.")


# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


try: # Algoritmo para solicitar un número y mostrar el resultado
    num = int(input("Introduce un número entero positivo: "))
    if num < 0:
        print("Por favor, introduce un número entero positivo.")
    elif num == 0:
        print("0 en binario es: 0")
    else:
        binario = decimal_a_binario(num)
        print(f"{num} en binario es: {binario}")
except ValueError:
    print("Entrada no válida. Debes introducir un número entero.")

# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# Función recursiva para verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# Función recursiva para sumar los dígitos de un número
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# Función recursiva para contar el total de bloques necesarios para construir la pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

# Función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)

