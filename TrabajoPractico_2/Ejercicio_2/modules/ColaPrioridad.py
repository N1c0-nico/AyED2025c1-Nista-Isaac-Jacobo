from modules.monticulo import MonticuloBinario

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.mapa = {}  # clave -> valor
        self.tamano = 0

    def encolar(self, clave, valor):
        if clave in self.mapa:
            raise KeyError("La clave ya existe.")
        self.mapa[clave] = valor
        self.monticulo.insertar((clave, valor))
        self.tamano += 1

    def desencolar(self, clave):
        if clave not in self.mapa:
            return
        del self.mapa[clave]
        self.tamano -= 1
        # No se elimina directamente del montículo: se ignora en lecturas

    def obtener(self, clave):
        return self.mapa[clave]

    def __iter__(self):
        # Devuelve un iterador sobre los pares (clave, valor), ordenados por clave
        return iter(sorted(self.mapa.items()))
