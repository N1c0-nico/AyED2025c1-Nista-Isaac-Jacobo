def bubble_sort(lista):
    n = len(lista)  # Guarda la longitud de la lista
    for i in range(n):  # Recorre la lista hasta que esté ordenada
        swapped = False  # Bandera para detectar si hubo algún intercambio
        for j in range(0, n - i - 1):  # Compara elementos adyacentes
            if lista[j] > lista[j + 1]:  # Si están en orden incorrecto...
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # ...los intercambia
                swapped = True  # Marca que hubo un intercambio
        if not swapped:
            break  # Si no hubo intercambios, la lista ya está ordenada
    return lista  # Devuelve la lista ordenada
