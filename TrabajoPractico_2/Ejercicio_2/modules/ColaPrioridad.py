from modules.arbolAVL import ArbolBinarioBusqueda 

class ColaDePrioridad:
    def __init__(self): # Creamos la clase de ColaDePrioridad y le añadimos un árbol
        self.arbol = ArbolBinarioBusqueda()

    def encolar(self, clave, valor): # Creamos una función encargada de añadir elementos a la cosa
        self.arbol.insertar(clave, valor)

    def desencolar(self, clave): # Creamos una función encargada de eliminar lementos de la cola
        self.arbol.eliminar(clave)

    def obtener(self, clave): # Creamos una clase que devuelve el valor asociado a un elemento de la cola
        return self.arbol.buscar(clave)

    def __iter__(self): # Función encargada de iterar dentro de la cola
        return iter(self.arbol)

    @property
    def tamano(self): # Propiedad encargada de devolver la cantidad de elementos en la cola
        return len(self.arbol)
