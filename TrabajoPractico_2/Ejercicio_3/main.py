from collections import defaultdict
from modules.prim import prim
from modules.arbolito import arbol_difusion

# Carga la red de aldeas desde el archivo de texto
def cargar_red_aldeas(archivo):
    red_aldeas = defaultdict(list)
    with open(archivo, "r") as f:
        for linea in f:
            partes = linea.strip().split(", ")
            if len(partes) == 3:
                origen, destino, leguas = partes
                leguas = int(leguas)
                red_aldeas[origen].append((destino, leguas))
                red_aldeas[destino].append((origen, leguas))  # Es no dirigido
    return red_aldeas

# Muestra los resultados del plan de entrega de mensajes
def mostrar_resultados(distancia_minima, camino_mas_corto, red_reenvio):
    aldeas = sorted(distancia_minima.keys())

    print(" Listado de aldeas en orden alfabético:\n")
    for aldea in aldeas:
        print(f" - {aldea}")

    print("\n Plan de difusión del mensaje:\n")
    for aldea in aldeas:
        aldeas_que_reciben = red_reenvio.get(aldea, [])
        aldea_emisora = camino_mas_corto.get(aldea, None)

        if aldea == "Peligros":
            print(f"{aldea:<15} envía a: {', '.join(sorted(aldeas_que_reciben)) if aldeas_que_reciben else 'Nadie'}")
        else:
            print(f"{aldea:<15} recibe de: {aldea_emisora if aldea_emisora else 'Nadie':<15}  envía a: {', '.join(sorted(aldeas_que_reciben)) if aldeas_que_reciben else 'Nadie'}")

    total_leguas = sum(distancia_minima.values())
    print(f"\n Suma total de distancias recorridas por todas las palomas: {total_leguas} leguas")

# Ejecución principal
red_aldeas = cargar_red_aldeas("aldeas.txt")
distancia_minima, camino_mas_corto = prim(red_aldeas, "Peligros")
red_reenvio = arbol_difusion(camino_mas_corto)
mostrar_resultados(distancia_minima, camino_mas_corto, red_reenvio)
