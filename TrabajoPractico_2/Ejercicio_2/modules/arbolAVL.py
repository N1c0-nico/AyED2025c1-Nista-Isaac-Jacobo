class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        # Inicializa un nodo del árbol con su clave, valor, hijos y padre
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.balance = 0  # balance para AVL (diferencia de alturas)

    # Métodos de consulta sobre el nodo
    def tieneHijoIzquierdo(self): return self.hijoIzquierdo is not None  # Retorna True si tiene hijo izquierdo
    def tieneHijoDerecho(self): return self.hijoDerecho is not None  # Retorna True si tiene hijo derecho
    def esHijoIzquierdo(self): return self.padre and self.padre.hijoIzquierdo == self  # True si es hijo izquierdo
    def esHijoDerecho(self): return self.padre and self.padre.hijoDerecho == self  # True si es hijo derecho
    def esRaiz(self): return self.padre is None  # True si es la raíz del árbol
    def esHoja(self): return not (self.hijoDerecho or self.hijoIzquierdo)  # True si no tiene hijos
    def tieneAlgunHijo(self): return self.hijoDerecho or self.hijoIzquierdo  # True si tiene al menos un hijo
    def tieneAmbosHijos(self): return self.hijoDerecho and self.hijoIzquierdo  # True si tiene dos hijos

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        # Reemplaza los datos del nodo con nuevos valores
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self  # Actualiza la referencia al padre
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self  # Actualiza la referencia al padre

from modules.arbolAVL import NodoArbol

class ArbolBinarioBusqueda:
    def __init__(self):
        # Inicializa un árbol vacío
        self.raiz = None
        self.tamano = 0

    def __len__(self):
        # Devuelve la cantidad de nodos en el árbol
        return self.tamano

    def insertar(self, clave, valor):
        # Inserta un nodo nuevo con clave y valor en el árbol
        if not self.raiz:
            self.raiz = NodoArbol(clave, valor)  # Si el árbol está vacío, crea la raíz
        else:
            self._insertar(clave, valor, self.raiz)  # Llama al método recursivo
        self.tamano += 1

    def _insertar(self, clave, valor, nodoActual):
        # Inserta un nodo en la posición correcta recursivamente
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._insertar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
                self._actualizarBalance(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._insertar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
                self._actualizarBalance(nodoActual.hijoDerecho)

    def _actualizarBalance(self, nodo):
        # Actualiza el factor de balance del nodo e intenta re-balancear si es necesario
        if nodo.balance > 1 or nodo.balance < -1:
            self._rebalancear(nodo)
            return
        if nodo.padre:
            if nodo.esHijoIzquierdo():
                nodo.padre.balance += 1
            elif nodo.esHijoDerecho():
                nodo.padre.balance -= 1

            if nodo.padre.balance != 0:
                self._actualizarBalance(nodo.padre)

    def _rebalancear(self, nodo):
        # Realiza las rotaciones necesarias para balancear el árbol AVL
        if nodo.balance < 0:
            if nodo.hijoDerecho.balance > 0:
                self._rotacionDerecha(nodo.hijoDerecho)
                self._rotacionIzquierda(nodo)
            else:
                self._rotacionIzquierda(nodo)
        elif nodo.balance > 0:
            if nodo.hijoIzquierdo.balance < 0:
                self._rotacionIzquierda(nodo.hijoIzquierdo)
                self._rotacionDerecha(nodo)
            else:
                self._rotacionDerecha(nodo)

    def _rotacionIzquierda(self, rotRaiz):
        # Realiza una rotación simple a la izquierda
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        # Actualiza los factores de balance
        rotRaiz.balance = rotRaiz.balance + 1 - min(nuevaRaiz.balance, 0)
        nuevaRaiz.balance = nuevaRaiz.balance + 1 + max(rotRaiz.balance, 0)

    def _rotacionDerecha(self, rotRaiz):
        # Realiza una rotación simple a la derecha
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        # Actualiza los factores de balance
        rotRaiz.balance = rotRaiz.balance - 1 - max(nuevaRaiz.balance, 0)
        nuevaRaiz.balance = nuevaRaiz.balance - 1 + min(rotRaiz.balance, 0)

    def buscar(self, clave):
        # Busca el valor asociado a una clave
        return self._buscar(clave, self.raiz)

    def _buscar(self, clave, nodo):
        # Búsqueda recursiva de una clave
        if nodo is None:
            raise KeyError("Clave no encontrada")
        if clave == nodo.clave:
            return nodo.cargaUtil
        elif clave < nodo.clave:
            return self._buscar(clave, nodo.hijoIzquierdo)
        else:
            return self._buscar(clave, nodo.hijoDerecho)

    def eliminar(self, clave):
        # Elimina un nodo por su clave
        nodo = self._buscar_nodo(clave, self.raiz)
        if nodo:
            self._remover(nodo)
            self.tamano -= 1

    def _buscar_nodo(self, clave, nodo):
        # Devuelve el nodo con la clave dada
        if nodo is None:
            raise KeyError("Clave no encontrada")
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self._buscar_nodo(clave, nodo.hijoIzquierdo)
        else:
            return self._buscar_nodo(clave, nodo.hijoDerecho)

    def _remover(self, nodo):
        # Lógica de eliminación de un nodo en el árbol AVL
        if nodo.esHoja():  # Si es hoja
            if nodo.esRaiz():
                self.raiz = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = None
            else:
                nodo.padre.hijoDerecho = None
        elif nodo.tieneAmbosHijos():  # Si tiene dos hijos
            sucesor = self._minimo(nodo.hijoDerecho)
            nodo.clave = sucesor.clave
            nodo.cargaUtil = sucesor.cargaUtil
            self._remover(sucesor)  # Elimina el sucesor recursivamente
        else:
            hijo = nodo.hijoIzquierdo if nodo.tieneHijoIzquierdo() else nodo.hijoDerecho
            if nodo.esRaiz():
                self.raiz = hijo
                hijo.padre = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = hijo
            else:
                nodo.padre.hijoDerecho = hijo
            hijo.padre = nodo.padre

    def _minimo(self, nodo):
        # Encuentra el nodo con la clave mínima a partir del nodo dado
        actual = nodo
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        # Permite iterar sobre el árbol en orden
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        # Recorrido inorden del árbol (izquierda, nodo, derecha)
        if nodo:
            yield from self._inorden(nodo.hijoIzquierdo)
            yield (nodo.clave, nodo.cargaUtil)
            yield from self._inorden(nodo.hijoDerecho)
