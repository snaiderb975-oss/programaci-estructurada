def cargar_datos():

    lista = []

    for i in range(5):

        numero = int(input("Ingrese un número: "))

        lista.append(numero)

    return lista


# Programa principal
datos = cargar_datos()

print(datos)



def filtrar_elementos(lista):

    pares = []

    for elemento in lista:

        if elemento % 2 == 0:
            pares.append(elemento)

    return pares


# Programa principal
numeros = [10, 7, 4, 9, 20]

resultado = filtrar_elementos(numeros)

print(resultado)



def procesar_calculos(lista):

    suma = 0

    for elemento in lista:

        suma = suma + elemento

    return suma


# Programa principal
numeros = [10, 20, 30, 40]

resultado = procesar_calculos(numeros)

print("La suma es:", resultado)


# ---------------------------------
# CARGAR DATOS
# ---------------------------------
def cargar_datos():

    lista = []

    for i in range(5):

        numero = int(input("Ingrese un número: "))

        lista.append(numero)

    return lista


# ---------------------------------
# FILTRAR PARES
# ---------------------------------
def filtrar_elementos(lista):

    pares = []

    for elemento in lista:

        if elemento % 2 == 0:
            pares.append(elemento)

    return pares


# ---------------------------------
# PROCESAR CÁLCULOS
# ---------------------------------
def procesar_calculos(lista):

    suma = 0

    for elemento in lista:

        suma = suma + elemento

    promedio = suma / len(lista)

    return suma, promedio


# ---------------------------------
# ORDENAR LISTA
# ---------------------------------
def ordenar_lista(lista):

    lista.sort()

    return lista


# ---------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------
datos = cargar_datos()

filtrados = filtrar_elementos(datos)

suma, promedio = procesar_calculos(datos)

ordenados = ordenar_lista(datos)

print("Lista original:", datos)
print("Lista filtrada:", filtrados)
print("Suma:", suma)
print("Promedio:", promedio)
print("Lista ordenada:", ordenados)
