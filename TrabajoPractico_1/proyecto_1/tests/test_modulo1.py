# Archivo de test para realizar pruebas unitarias del modulo1
import time
from modules import Funciones, BubbleSort, QuickSort
lista = Funciones.Crearlista (1000)
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