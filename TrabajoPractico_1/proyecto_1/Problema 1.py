from matplotlib import pyplot as plt
from modules.BubbleSort import bubble_sort
from modules.QuickSort import quicksort
from modules.Funciones import Tiempos
from modules.RadixSort import radix_sort
from modules import Funciones
import time 

lista = Funciones.Crearlista(500)
lista2 = lista
lista3 = lista
lista4 = lista

#Time BubbleSort
inicio = time.perf_counter()
bubble_sort(lista)
fin = time.perf_counter()
tiempo_ejecucionBubble = fin - inicio
print(f"Tiempo de ejecución Bubblesort: {tiempo_ejecucionBubble:.4f} segundos")

#Time QuickSort
inicio = time.perf_counter()
quicksort(lista2)
fin = time.perf_counter()
tiempo_ejecucionQuick = fin - inicio
print(f"Tiempo de ejecución Quicksort: {tiempo_ejecucionQuick:.4f} segundos")

#Time RadixSort
inicio = time.perf_counter()
quicksort(lista3)
fin = time.perf_counter()
tiempo_ejecucionRadix = fin - inicio
print(f"Tiempo de ejecución Radixsort: {tiempo_ejecucionRadix:.4f} segundos")

#Time Sorted
inicio = time.perf_counter()
sorted(lista4)
fin = time.perf_counter()
tiempo_ejecucionSorted = fin - inicio
print(f"Tiempo de ejecución Sorted: {tiempo_ejecucionSorted:.4f} segundos")

ListaDeTiempos = [tiempo_ejecucionBubble, tiempo_ejecucionQuick, tiempo_ejecucionRadix, tiempo_ejecucionSorted]



tamanos = [1, 10, 100, 200, 500, 700, 1000]
lista_bubble =  Tiempos (bubble_sort, tamanos)
lista_quicksort =  Tiempos (quicksort, tamanos)
lista_Radix = Tiempos(radix_sort, tamanos)
lista_Sorted = Tiempos(sorted, tamanos)
listas_ordenadas = [(lista_bubble, "BubbleSort"), (lista_quicksort, "QuickSort"), (lista_Radix, "RadixSort"), (lista_Sorted, "Sorted")]
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
