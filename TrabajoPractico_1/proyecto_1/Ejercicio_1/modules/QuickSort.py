def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]
    return quicksort(left) + middle + quicksort(right)# Implementación del algoritmo QuickSort (ordenamiento rápido)
def quicksort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Se elige un pivote (en este caso, el elemento del medio)
    pivot = lista[len(lista) // 2]

    # Se crean tres listas:
    # - 'left' con los elementos menores al pivote
    # - 'middle' con los elementos iguales al pivote
    # - 'right' con los elementos mayores al pivote
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]

    # Se aplica quicksort recursivamente a 'left' y 'right'
    # Luego se concatenan los resultados con 'middle' al centro
    return quicksort(left) + middle + quicksort(right)
