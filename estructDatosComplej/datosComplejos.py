#  Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios

# frutas = list(precios_frutas.keys())
# print(frutas)

# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
# contactos = {"Juan" : "123456", "Ana": "987654"}
# consultar: "Juan" -> muestra "123456"

# Crear un diccionario vacío para los contactos
contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    contactos[nombre] = numero

# Consultar un número telefónico
nombre_busqueda = input("Ingresá el nombre del contacto que querés buscar: ")

# Mostrar el número si existe
if nombre_busqueda in contactos:
    print(f"El número de {nombre_busqueda} es: {contactos[nombre_busqueda]}")
else:
    print(f"No se encontró un contacto con el nombre '{nombre_busqueda}'.")

# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:

# Entrada -> "hola mundo hola"
# Salida:
# palabras_unicas: {"hola", "mundo"}
# Recuento: {"hola": 2, "mundo": 1}

# Solicitar frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Crear un conjunto de palabras únicas
palabras_unicas = set(palabras)

# Crear un diccionario para contar apariciones
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:
# alumnos = {
#      "Sofia": (10, 9, 8),
#      "Luis": (6, 7, 7)
# }

# Crear diccionario vacío
alumnos = {}

# Cargar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    # Pedir las 3 notas
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    # Guardar en el diccionario como tupla
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar promedios
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Ejemplo de sets con estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Juan", "Luis", "María"}
parcial2 = {"Luis", "María", "Carlos", "Sofía"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1.intersection(parcial2)

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1.symmetric_difference(parcial2)

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1.union(parcial2)

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario inicial con algunos productos
stock = {
    "manzanas": 50,
    "naranjas": 30,
    "bananas": 20
}

# Consultar stock
producto = input("Ingresá el nombre del producto para consultar: ").lower()

if producto in stock:
    print(f"Stock de {producto}: {stock[producto]} unidades")
    
    # Agregar unidades
    agregar = input("¿Querés agregar unidades a este producto? (si/no): ").lower()
    if agregar == "si":
        unidades = int(input("Ingresá la cantidad a agregar: "))
        stock[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock[producto]} unidades")
else:
    # Agregar nuevo producto
    print(f"El producto '{producto}' no existe.")
    agregar_nuevo = input("¿Querés agregarlo al stock? (si/no): ").lower()
    if agregar_nuevo == "si":
        unidades = int(input("Ingresá la cantidad inicial: "))
        stock[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")

print("\nStock final:", stock)

# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:

# agenda = {
#     ("lunes", "10:00"): "Reunión",
#     ("martes", "15:00"): "clase de ingles"
# }
# Permití consultar qué actividad hay en cierto día y hora.

# Agenda ejemplo
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "clase de ingles"
}

# Consultar actividad
dia = input("Ingresá el día (ej: lunes): ").lower()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"En {dia} a las {hora} tenés: {agenda[clave]}")
else:
    print(f"No hay actividades programadas para {dia} a las {hora}.")

# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:
# original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
# invertido = {"Buenos Aires: "Argentina, "Santiago": "Chile"}

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

# Invertir claves y valores
invertido = {capital: pais for pais, capital in original.items()}

print(invertido)


