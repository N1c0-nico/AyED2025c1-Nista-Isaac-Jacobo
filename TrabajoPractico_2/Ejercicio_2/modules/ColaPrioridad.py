from modules.arbolAVL import ArbolBinarioBusqueda

class ColaDePrioridad:
    def __init__(self):
        self.arbol = ArbolBinarioBusqueda()

    def encolar(self, clave, valor):
        self.arbol.insertar(clave, valor)

    def desencolar(self, clave):
        self.arbol.eliminar(clave)

    def obtener(self, clave):
        return self.arbol.buscar(clave)

    def __iter__(self):
        return iter(self.arbol)

    @property
    def tamano(self):
        return len(self.arbol)