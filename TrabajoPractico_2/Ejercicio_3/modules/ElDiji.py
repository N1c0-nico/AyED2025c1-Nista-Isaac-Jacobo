from modules.monticules import MonticuloBinario
def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {}
    cola = MonticuloBinario()
    cola.insertar(0, inicio)

    while not cola.esta_vacio():
        distancia_actual, nodo_actual = cola.extraer()

        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                cola.insertar(distancia, vecino)

    return distancias, predecesores
