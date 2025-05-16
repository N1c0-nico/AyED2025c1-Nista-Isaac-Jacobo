from random import randint  
import time  

# Esta función implementa el algoritmo de ordenamiento por selección.
# Coloca el elemento más grande al final en cada pasada.
def ordenamiento_por_seleccion(una_lista):
    # Se recorre la lista desde el final hasta el principio
    for llenar_ranura in range(len(una_lista) - 1, 0, -1):
        posicion_del_mayor = 0  # Se asume que el primer elemento es el mayor

        # Se busca el elemento más grande en la parte no ordenada de la lista
        for ubicacion in range(1, llenar_ranura + 1):
            if una_lista[ubicacion] > una_lista[posicion_del_mayor]:
                posicion_del_mayor = ubicacion  # Se actualiza la posición del mayor encontrado

        # Se intercambia el elemento más grande con el que está en la posición final de la pasada
        temp = una_lista[llenar_ranura]
        una_lista[llenar_ranura] = una_lista[posicion_del_mayor]
        una_lista[posicion_del_mayor] = temp

    return una_lista  # Se devuelve la lista ya ordenada

# Este bloque se ejecuta solo si se corre el script directamente
if __name__ == '__main__':
    mi_lista = [5, 3, 8, 6, 2, 7, 4, 1]  # Lista de ejemplo a ordenar
    print(ordenamiento_por_seleccion(mi_lista))  # Imprime la lista ya ordenada
