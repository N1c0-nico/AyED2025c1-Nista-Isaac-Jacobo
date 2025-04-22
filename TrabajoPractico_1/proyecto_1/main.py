from matplotlib import pyplot as plt
from modules.BubbleSort import bubble_sort
from modules.QuickSort import quicksort
from modules.Funciones import Tiempos
from modules.RadixSort import radix_sort


"""
lista2 = lista
#lista3 = lista

#Time BubbleSort
inicio = time.perf_counter()
BubbleSort.bubble_sort(lista)
fin = time.perf_counter()
tiempo_ejecucionBubble = fin - inicio
print(f"Tiempo de ejecución Bubblesort: {tiempo_ejecucionBubble:.4f} segundos")

#Time QuickSort
inicio = time.perf_counter()
QuickSort.quicksort(lista2)
fin = time.perf_counter()
tiempo_ejecucionQuick = fin - inicio
print(f"Tiempo de ejecución Quicksort: {tiempo_ejecucionQuick:.4f} segundos")

ListaDeTiempos = [tiempo_ejecucionBubble, tiempo_ejecucionQuick]
"""


tamanos = [1, 10, 100, 200, 500, 700, 1000]
lista_bubble =  Tiempos (bubble_sort, tamanos)
lista_quicksort =  Tiempos (quicksort, tamanos)
lista_Radix = Tiempos(radix_sort, tamanos)
listas_ordenadas = [(lista_bubble, "BubbleSort"), (lista_quicksort, "QuickSort"), (lista_Radix, "RadixSort")]
#lista_metodos_ord = [(bubble_sort, lista_bubble),(quicksort, lista_quicksort)]


def graficar_tiempos(listas_ordenadas):
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    
    plt.figure(figsize=(10, 6))

    for lista, etiqueta in listas_ordenadas:

        # plot es para graficar los tiempos de ordenamiento
        # plot es el método de matplotlib para graficar
        # marker='o' es para poner un punto en cada coordenada
        plt.plot(tamanos, lista, marker='o', label = etiqueta)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()

graficar_tiempos(listas_ordenadas)