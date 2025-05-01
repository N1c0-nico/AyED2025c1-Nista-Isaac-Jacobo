import time
from matplotlib import pyplot as plt
from modules import Funciones
from modules.ClaseNodoYLDE import ListaDobleEnlazada

def Crearlistal(n):
    lista = ListaDobleEnlazada()
    for i in range(n):
        lista.agregar_al_final(i)
    return lista

# Aseguramos que cada prueba use una nueva lista
def medir_tiempos_por_funcion(funcion, tamanos):
    tiempos = []
    for n in tamanos:
        lista = Crearlistal(n)
        if funcion == ListaDobleEnlazada.invertir or funcion == ListaDobleEnlazada.copiar:
            lista = lista.copiar()  # Para que no afecte otras pruebas

        inicio = time.perf_counter()
        funcion(lista)
        fin = time.perf_counter()

        tiempo = fin - inicio
        tiempos.append(tiempo)
        print(f"Tamaño: {n}, Tiempo para {funcion.__name__}: {tiempo:.6f} segundos")
    return tiempos

tamanos = [1, 10, 100, 200, 500, 700, 1000]

# Medimos los tiempos para cada método
tiempos_len = medir_tiempos_por_funcion(ListaDobleEnlazada.__len__, tamanos)
tiempos_invertir = medir_tiempos_por_funcion(ListaDobleEnlazada.invertir, tamanos)
tiempos_copiar = medir_tiempos_por_funcion(ListaDobleEnlazada.copiar, tamanos)

# Función para graficar
def graficar_tiempos(listas_ordenadas, tamanos):
    plt.figure(figsize=(10, 6))
    for lista, etiqueta in listas_ordenadas:
        plt.plot(tamanos, lista, marker='o', label=etiqueta)
    plt.xlabel('Tamaño de la lista (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('N vs Tiempo de ejecución')
    plt.legend()
    plt.grid()
    plt.show()

# Agrupamos resultados
listas_ordenadas = [
    (tiempos_len, 'len()'),
    (tiempos_invertir, 'invertir()'),
    (tiempos_copiar, 'copiar()')
]

# Imprimimos listas completas de tiempos
print("\nResumen de tiempos:")
for nombre, tiempos in zip(["len()", "invertir()", "copiar()"], [tiempos_len, tiempos_invertir, tiempos_copiar]):
    for n, t in zip(tamanos, tiempos):
        print(f"{nombre} - Tamaño {n}: {t:.6f} segundos")

# Graficamos
graficar_tiempos(listas_ordenadas, tamanos)
