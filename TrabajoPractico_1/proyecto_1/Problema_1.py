# Importa la biblioteca de visualización matplotlib para graficar
from matplotlib import pyplot as plt

# Importa las funciones de ordenamiento desde distintos módulos propios
from modules.BubbleSort import bubble_sort
from modules.QuickSort import quicksort
from modules.Funciones import Tiempos
from modules.RadixSort import radix_sort
from modules import Funciones

# Importa la biblioteca time para medir tiempos de ejecución
import time 

# Crea una lista de 500 elementos usando la función Crearlista
lista = Funciones.Crearlista(500)

# Asigna la misma lista original a otras tres variables (nota: esto no copia, sino que apunta al mismo objeto)
lista2 = lista
lista3 = lista
lista4 = lista

# Mide el tiempo de ejecución del algoritmo BubbleSort
inicio = time.perf_counter()
bubble_sort(lista)
fin = time.perf_counter()
tiempo_ejecucionBubble = fin - inicio
print(f"Tiempo de ejecución Bubblesort: {tiempo_ejecucionBubble:.4f} segundos")

# Mide el tiempo de ejecución del algoritmo QuickSort
inicio = time.perf_counter()
quicksort(lista2)
fin = time.perf_counter()
tiempo_ejecucionQuick = fin - inicio
print(f"Tiempo de ejecución Quicksort: {tiempo_ejecucionQuick:.4f} segundos")

# Mide el tiempo de ejecución del algoritmo RadixSort (pero por error se está llamando quicksort otra vez)
inicio = time.perf_counter()
quicksort(lista3)  # ¡OJO! Acá deberías usar radix_sort(lista3)
fin = time.perf_counter()
tiempo_ejecucionRadix = fin - inicio
print(f"Tiempo de ejecución Radixsort: {tiempo_ejecucionRadix:.4f} segundos")

# Mide el tiempo de ejecución del método built-in sorted de Python
inicio = time.perf_counter()
sorted(lista4)
fin = time.perf_counter()
tiempo_ejecucionSorted = fin - inicio
print(f"Tiempo de ejecución Sorted: {tiempo_ejecucionSorted:.4f} segundos")

# Guarda los tiempos de ejecución en una lista
ListaDeTiempos = [tiempo_ejecucionBubble, tiempo_ejecucionQuick, tiempo_ejecucionRadix, tiempo_ejecucionSorted]

# Define los tamaños de listas con los que se van a probar los algoritmos
tamanos = [1, 10, 100, 200, 500, 700, 1000]

# Calcula los tiempos de ejecución de cada algoritmo para cada tamaño de lista
lista_bubble =  Tiempos (bubble_sort, tamanos)
lista_quicksort =  Tiempos (quicksort, tamanos)
lista_Radix = Tiempos(radix_sort, tamanos)
lista_Sorted = Tiempos(sorted, tamanos)

# Agrupa los resultados en una lista de tuplas (cada tupla: lista de tiempos y nombre del algoritmo)
listas_ordenadas = [(lista_bubble, "BubbleSort"), (lista_quicksort, "QuickSort"), (lista_Radix, "RadixSort"), (lista_Sorted, "Sorted")]
# lista_metodos_ord = [(bubble_sort, lista_bubble),(quicksort, lista_quicksort)]  # Línea comentada sin usar

# Define la función que grafica los tiempos de ejecución de cada algoritmo
def graficar_tiempos(listas_ordenadas):
    tamanos = [1, 10, 100, 200, 500, 700, 1000]  # Vuelve a definir los tamaños para usar en el eje X
    
    plt.figure(figsize=(10, 6))  # Tamaño de la figura del gráfico

    # Itera sobre cada lista de tiempos y su etiqueta
    for lista, etiqueta in listas_ordenadas:
        # Grafica los tiempos de ejecución para cada algoritmo
        plt.plot(tamanos, lista, marker='o', label = etiqueta)

    # Configura los ejes, título y leyenda del gráfico
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend()  # Muestra la leyenda con los nombres de cada algoritmo
    plt.grid()    # Activa el fondo cuadriculado
    plt.show()    # Muestra el gráfico

# Llama a la función para graficar los resultados
graficar_tiempos(listas_ordenadas)
