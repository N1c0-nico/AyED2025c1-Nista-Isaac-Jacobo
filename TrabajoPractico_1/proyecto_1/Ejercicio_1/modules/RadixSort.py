
# Esta función realiza una ordenación estable basada en el dígito actual (exponente)
def counting_sort_por_digito(lista, exponente):
    n = len(lista)
    salida = [0] * n  # Lista de salida ordenada
    conteo = [0] * 10  # Conteo de dígitos de 0 a 9

    # Contar ocurrencias de cada dígito en la posición actual (exponente)
    for i in range(n):
        indice = (lista[i] // exponente) % 10  # Extrae el dígito relevante
        conteo[indice] += 1

    # Acumula los conteos para determinar posiciones
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir la lista de salida en orden estable (recorriendo de atrás hacia adelante)
    for i in reversed(range(n)):
        indice = (lista[i] // exponente) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1

    # Copiar la salida a la lista original
    for i in range(n):
        lista[i] = salida[i]


# Esta función implementa el algoritmo Radix Sort
# Ordena por cada dígito (de menor a mayor significancia)
def radix_sort(lista):
    if len(lista) == 0:
        return lista

    max_num = max(lista)  # Encuentra el número más grande
    exponente = 1  # exponente representa la posición del dígito actual: 1=unidades, 10=decenas...

    # Itera mientras haya dígitos en el número más grande
    while max_num // exponente > 0:
        counting_sort_por_digito(lista, exponente)  # Ordena por el dígito actual
        exponente *= 10  # Pasa al siguiente dígito

    return lista

