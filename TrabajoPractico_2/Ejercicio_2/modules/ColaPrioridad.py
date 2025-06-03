from datetime import datetime
from modules.LaArboleda import ArbolAVL

class ColaDePrioridad:
    def __init__(self):
        self.arbol = ArbolAVL()
        self._tamano = 0

    def encolar(self, clave, valor):
        self.arbol.insertar(clave, valor)
        self._tamano += 1

    def desencolar(self, clave):
        try:
            self.arbol.eliminar(clave)
            self._tamano -= 1
        except KeyError:
            pass

    def obtener(self, clave):
        return self.arbol.obtener(clave)

    def __iter__(self):
        return iter(sorted(self.arbol.en_rango(datetime.min, datetime.max)))

    @property
    def tamano(self):
        return self._tamano
