from collections import defaultdict
def arbol_difusion(predecesores):
    hijos = defaultdict(list)
    for aldea, padre in predecesores.items():
        hijos[padre].append(aldea)
    return hijos
