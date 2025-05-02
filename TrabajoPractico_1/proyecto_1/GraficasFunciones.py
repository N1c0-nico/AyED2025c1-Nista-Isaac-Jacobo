import time
from matplotlib import pyplot as plt
from modules import Funciones  # Asegúrate de tener este módulo disponible
from modules.ClaseNodoYLDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

# Crear lista de tamaño n usando ListaDobleEnlazada
def Crearlistal(n):
    lista = ListaDobleEnlazada()
    for i in range(n):
        lista.agregar_al_final(i)  # Agrega números secuenciales
    return lista

# Función que mide los tiempos de ejecución de un método para varias listas de tamaño creciente
def medir_tiempos_por_funcion(funcion, tamanos):
    tiempos = []  # Lista para almacenar los tiempos de ejecución
    for n in tamanos:
        lista = Crearlistal(n)  # Crea una lista de tamaño n
        # Si la función que estamos midiendo es 'invertir' o 'copiar', hacemos una copia para evitar cambios en la lista original
        if funcion == ListaDobleEnlazada.invertir or funcion == ListaDobleEnlazada.copiar:
            lista = lista.copiar()  # Realiza una copia de la lista para no modificarla

        # Medimos el tiempo de ejecución de la función
        inicio = time.perf_counter()
        funcion(lista)  # Ejecuta la función con la lista
        fin = time.perf_counter()

        tiempo = fin - inicio  # Calcula el tiempo en segundos
        tiempos.append(tiempo)  # Añade el tiempo a la lista de tiempos
        print(f"Tamaño: {n}, Tiempo para {funcion.__name__}: {tiempo:.6f} segundos")
    return tiempos

# Definimos los tamaños de lista para las pruebas
tamanos = [1, 10, 100, 200, 500, 700, 1000]

# Medimos los tiempos de ejecución de los tres métodos
tiempos_len = medir_tiempos_por_funcion(ListaDobleEnlazada.__len__, tamanos)  # Tiempo de len()
tiempos_invertir = medir_tiempos_por_funcion(ListaDobleEnlazada.invertir, tamanos)  # Tiempo de invertir()
tiempos_copiar = medir_tiempos_por_funcion(ListaDobleEnlazada.copiar, tamanos)  # Tiempo de copiar()

# Función para graficar los resultados
def graficar_tiempos(listas_ordenadas, tamanos):
    plt.figure(figsize=(10, 6))  # Define el tamaño de la figura
    # Graficamos los tiempos para cada lista
    for lista, etiqueta in listas_ordenadas:
        plt.plot(tamanos, lista, marker='o', label=etiqueta)  # Plotea cada lista con su etiqueta
    plt.xlabel('Tamaño de la lista (N)')  # Etiqueta para el eje X
    plt.ylabel('Tiempo (segundos)')  # Etiqueta para el eje Y
    plt.title('N vs Tiempo de ejecución')  # Título del gráfico
    plt.legend()  # Muestra la leyenda
    plt.grid()  # Muestra la cuadrícula
    plt.show()  # Muestra el gráfico

# Agrupamos los resultados de los tiempos para cada método
listas_ordenadas = [
    (tiempos_len, 'len()'),
    (tiempos_invertir, 'invertir()'),
    (tiempos_copiar, 'copiar()')
]

# Imprimimos los resultados completos de los tiempos medidos
print("\nResumen de tiempos:")
for nombre, tiempos in zip(["len()", "invertir()", "copiar()"], [tiempos_len, tiempos_invertir, tiempos_copiar]):
    for n, t in zip(tamanos, tiempos):
        print(f"{nombre} - Tamaño {n}: {t:.6f} segundos")

# Graficamos los resultados
graficar_tiempos(listas_ordenadas, tamanos)
