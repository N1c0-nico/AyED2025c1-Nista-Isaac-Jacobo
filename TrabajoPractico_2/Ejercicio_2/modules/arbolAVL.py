class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.balance = 0  # balance AVL

    # Métodos de consulta (mismos que ya tenías)
    def tieneHijoIzquierdo(self): return self.hijoIzquierdo is not None
    def tieneHijoDerecho(self): return self.hijoDerecho is not None
    def esHijoIzquierdo(self): return self.padre and self.padre.hijoIzquierdo == self
    def esHijoDerecho(self): return self.padre and self.padre.hijoDerecho == self
    def esRaiz(self): return self.padre is None
    def esHoja(self): return not (self.hijoDerecho or self.hijoIzquierdo)
    def tieneAlgunHijo(self): return self.hijoDerecho or self.hijoIzquierdo
    def tieneAmbosHijos(self): return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

from modules.arbolAVL import NodoArbol

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def __len__(self):
        return self.tamano

    def insertar(self, clave, valor):
        if not self.raiz:
            self.raiz = NodoArbol(clave, valor)
        else:
            self._insertar(clave, valor, self.raiz)
        self.tamano += 1

    def _insertar(self, clave, valor, nodoActual):
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
        rotRaiz.balance = rotRaiz.balance + 1 - min(nuevaRaiz.balance, 0)
        nuevaRaiz.balance = nuevaRaiz.balance + 1 + max(rotRaiz.balance, 0)

    def _rotacionDerecha(self, rotRaiz):
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
        rotRaiz.balance = rotRaiz.balance - 1 - max(nuevaRaiz.balance, 0)
        nuevaRaiz.balance = nuevaRaiz.balance - 1 + min(rotRaiz.balance, 0)

    def buscar(self, clave):
        return self._buscar(clave, self.raiz)

    def _buscar(self, clave, nodo):
        if nodo is None:
            raise KeyError("Clave no encontrada")
        if clave == nodo.clave:
            return nodo.cargaUtil
        elif clave < nodo.clave:
            return self._buscar(clave, nodo.hijoIzquierdo)
        else:
            return self._buscar(clave, nodo.hijoDerecho)

    def eliminar(self, clave):
        nodo = self._buscar_nodo(clave, self.raiz)
        if nodo:
            self._remover(nodo)
            self.tamano -= 1

    def _buscar_nodo(self, clave, nodo):
        if nodo is None:
            raise KeyError("Clave no encontrada")
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self._buscar_nodo(clave, nodo.hijoIzquierdo)
        else:
            return self._buscar_nodo(clave, nodo.hijoDerecho)

    def _remover(self, nodo):
        # Lógica de eliminación simplificada para AVL
        if nodo.esHoja():
            if nodo.esRaiz():
                self.raiz = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = None
            else:
                nodo.padre.hijoDerecho = None
        elif nodo.tieneAmbosHijos():
            sucesor = self._minimo(nodo.hijoDerecho)
            nodo.clave = sucesor.clave
            nodo.cargaUtil = sucesor.cargaUtil
            self._remover(sucesor)
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
        actual = nodo
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo:
            yield from self._inorden(nodo.hijoIzquierdo)
            yield (nodo.clave, nodo.cargaUtil)
            yield from self._inorden(nodo.hijoDerecho)