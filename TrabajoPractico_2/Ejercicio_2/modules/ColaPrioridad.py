from modules.arbolAVL import ArbolBinarioBusqueda  # Importa la clase ArbolBinarioBusqueda desde el módulo arbolAVL

class ColaDePrioridad:
    def __init__(self):
        # Inicializa una nueva instancia de ColaDePrioridad creando un árbol binario de búsqueda vacío
        self.arbol = ArbolBinarioBusqueda()

    def encolar(self, clave, valor):
        # Inserta un nuevo elemento en la cola de prioridad usando la clave para el orden y un valor asociado
        self.arbol.insertar(clave, valor)

    def desencolar(self, clave):
        # Elimina el elemento con la clave dada de la cola de prioridad, quitándolo del árbol
        self.arbol.eliminar(clave)

    def obtener(self, clave):
        # Busca y devuelve el valor asociado a la clave dada dentro del árbol (cola de prioridad)
        return self.arbol.buscar(clave)

    def __iter__(self):
        # Permite iterar sobre la cola de prioridad devolviendo un iterador sobre el árbol
        return iter(self.arbol)

    @property
    def tamano(self):
        # Propiedad que devuelve la cantidad de elementos actualmente almacenados en la cola de prioridad
        return len(self.arbol)
