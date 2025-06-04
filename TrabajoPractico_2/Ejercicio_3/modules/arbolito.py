from collections import defaultdict # Importamos defaultdict para que sea mas sencillo crear listas

def arbol_difusion(camino_mas_corto): # Construimos un árbol donde se almacenen las aldeas anteriores al mensaje
    
    red_reenvio = defaultdict(list)  # Diccionario que lista a qué aldeas reenviar el mensaje

    for aldea, predecesora in camino_mas_corto.items():
        red_reenvio[predecesora].append(aldea)  # La aldea predecesora reenvía a la actual
    
    return red_reenvio

