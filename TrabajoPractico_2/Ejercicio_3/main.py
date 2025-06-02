from collections import defaultdict
from modules.ElDiji import *
from modules.arbolito import arbol_difusion
def cargar_grafo(archivo):
    grafo = defaultdict(list)
    with open(archivo, "r") as f:
        for linea in f:
            partes = linea.strip().split(", ")
            if len(partes) == 3:
                origen, destino, peso = partes
                peso = int(peso)
                grafo[origen].append((destino, peso))
                grafo[destino].append((origen, peso))  # Es no dirigido
    return grafo

def mostrar_resultados(distancias, predecesores, hijos):
    aldeas = sorted(distancias.keys())

    print(" Listado de aldeas en orden alfabético:\n")
    for aldea in aldeas:
        print(f" - {aldea}")

    print("\n Plan de difusión del mensaje:\n")
    for aldea in aldeas:
        envia_a = hijos.get(aldea, [])
        recibe_de = predecesores.get(aldea, None)

        if aldea == "Peligros":
            print(f"{aldea:<15} envía a: {', '.join(sorted(envia_a)) if envia_a else 'Nadie'}")
        else:
            print(f"{aldea:<15} recibe de: {recibe_de if recibe_de else 'Nadie':<15}  envía a: {', '.join(sorted(envia_a)) if envia_a else 'Nadie'}")

    total_distancia = sum(distancias.values())
    print(f"\n Suma total de distancias recorridas por todas las palomas: {total_distancia} leguas")

grafo = cargar_grafo("aldeas.txt")
distancias, predecesores = dijkstra(grafo, "Peligros")
hijos = arbol_difusion(predecesores)
mostrar_resultados(distancias, predecesores, hijos)
