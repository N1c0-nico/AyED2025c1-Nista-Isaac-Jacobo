


# Función auxiliar que realiza una especie de "Counting Sort" sobre un dígito específico
# posición_digito = 1 para unidades, 10 para decenas, 100 para centenas, etc.
def ordenamiento_por_conteo_por_digito(lista, posicion_digito):
    n = len(lista)
    resultado = [0] * n  # Lista donde guardamos los números ya ordenados por el dígito actual
    conteo = [0] * 10  # Para contar cuántas veces aparece cada dígito (0-9) en esta posición

    # Paso 1: Contar las ocurrencias de cada dígito en la posición actual
    for i in range(n):
        indice = (lista[i] // posicion_digito) % 10  # Extraemos el dígito que nos interesa
        conteo[indice] += 1

    # Paso 2: Transformar el conteo en posiciones acumuladas
    # Esto permite saber en qué índice del arreglo ordenado debe ir cada elemento
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Paso 3: Construir la lista ordenada según el dígito actual
    # Lo hacemos en orden inverso para mantener la estabilidad del algoritmo
    i = n - 1
    while i >= 0:
        indice = (lista[i] // posicion_digito) % 10
        resultado[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    # Paso 4: Copiar el contenido ordenado de vuelta a la lista original
    for i in range(n):
        lista[i] = resultado[i]


# Función principal que implementa Radix Sort completo
# Utiliza la función anterior para ordenar según cada dígito, de menor a mayor significancia
def ordenamiento_radix(lista):
    # Paso 1: Encontrar el número más grande para saber cuántas veces debemos ordenar
    numero_maximo = max(lista)

    # Paso 2: Ordenar por cada dígito (unidades, decenas, centenas, etc.)
    posicion_digito = 1
    while numero_maximo // posicion_digito > 0:
        ordenamiento_por_conteo_por_digito(lista, posicion_digito)
        posicion_digito *= 10

"""
# Ejemplo de uso:
lista_numeros = [170, 45, 75, 90, 802, 24, 2, 66]
print("Antes:", lista_numeros)
ordenamiento_radix(lista_numeros)
print("Después:", lista_numeros)
"""