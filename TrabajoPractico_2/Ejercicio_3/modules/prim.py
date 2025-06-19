from modules.ColaPrioridad import ColaDePrioridad

def prim(red_aldeas, aldea_origen):
    visitadas = set()
    camino_mas_corto = {}
    distancia_minima = {aldea: float('inf') for aldea in red_aldeas}
    distancia_minima[aldea_origen] = 0

    cola = ColaDePrioridad()
    cola.encolar(0, aldea_origen)

    while not cola.esta_vacio():
        distancia_actual, aldea_actual = cola.desencolar()

        if aldea_actual in visitadas:
            continue

        visitadas.add(aldea_actual)

        for vecina, peso in red_aldeas[aldea_actual]:
            if vecina not in visitadas and peso < distancia_minima[vecina]:
                distancia_minima[vecina] = peso
                camino_mas_corto[vecina] = aldea_actual
                cola.encolar(peso, vecina)

    return distancia_minima, camino_mas_corto
