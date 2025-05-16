# Módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

# Función para crear una lista de n números aleatorios de 5 cifras
def Crearlista(n):
    import random
    lista = []
    for numero in range(n):  # Se repite n veces
        numero = random.randint(10000, 99999)  # Número aleatorio de 5 cifras
        lista.append(numero)  # Se agrega a la lista
    return lista  # Se retorna la lista generada

# Función que toma los tiempos de ejecución de un algoritmo de ordenamiento
def Tiempos(Ordenador, tamanos):
    import time
    import random
    aux = []  # Lista para guardar los tiempos de cada corrida

    for n in tamanos:  # Para cada tamaño en la lista de tamaños

        # Se crea una lista de n números aleatorios entre 1 y 10000
        datos = [random.randint(1, 10000) for _ in range(n)]

        # Se toma el tiempo antes de ordenar
        inicio = time.perf_counter()
        Ordenador(datos.copy())  # Se llama al algoritmo de ordenamiento con una copia de los datos
        fin = time.perf_counter()  # Se toma el tiempo después de ordenar

        aux.append(fin - inicio)  # Se guarda la diferencia de tiempo
    return aux  # Se devuelve la lista de tiempos
