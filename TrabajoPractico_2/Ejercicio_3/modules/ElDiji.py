from modules.monticules import MonticuloBinario


def dijkstra(red_aldeas, aldea_origen): # Creamos la dunción dijkstra para encontrar el camino mas corto
    distancia_minima = {aldea: float('inf') for aldea in red_aldeas}
    distancia_minima[aldea_origen] = 0  # Alclaramos que al empezar por la aldea de orígen la distancia es 0
    
    camino_mas_corto = {} # Diccionario para registrar de qué aldea viene cada una

    cola_prioridad = MonticuloBinario() # Creamos un montículo como cola de prioridad para seleccionar la próxima aldea
    cola_prioridad.insertar(0, aldea_origen)

    while not cola_prioridad.esta_vacio():
        distancia_actual, aldea_actual = cola_prioridad.extraer()

        # Verifica los vecinos de la aldea actual
        for aldea_vecina, leguas in red_aldeas[aldea_actual]:
            nueva_distancia = distancia_actual + leguas
            if nueva_distancia < distancia_minima[aldea_vecina]:
                distancia_minima[aldea_vecina] = nueva_distancia
                camino_mas_corto[aldea_vecina] = aldea_actual
                cola_prioridad.insertar(nueva_distancia, aldea_vecina)

    return distancia_minima, camino_mas_corto

