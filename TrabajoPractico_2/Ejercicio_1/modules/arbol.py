# modules/ordenamiento.py

class Arbol:
    def __init__(self, clave, valor):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.hijoDerecho is not None

    def esHoja(self):
        return not (self.tieneHijoIzquierdo() or self.tieneHijoDerecho())

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return self.padre is None

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class ColaPrioridad:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self, clave, valor):
        if self.raiz is None:
            self.raiz = Arbol(clave, valor)
        else:
            self._agregar(clave, valor, self.raiz)
        self.tamano += 1

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = Arbol(clave, valor)
                nodoActual.hijoIzquierdo.padre = nodoActual
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = Arbol(clave, valor)
                nodoActual.hijoDerecho.padre = nodoActual

    def _setitem_(self, clave, valor):
        self.agregar(clave, valor)

    def _getitem_(self, clave):
        return self.obtener(clave)

    def obtener(self, clave):
        nodo = self._buscar(clave, self.raiz)
        if nodo is None:
            raise Exception("Clave no encontrada")
        return nodo.cargaUtil

    def _buscar(self, clave, nodoActual):
        if nodoActual is None:
            return None
        elif clave == nodoActual.clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._buscar(clave, nodoActual.hijoIzquierdo)
        else:
            return self._buscar(clave, nodoActual.hijoDerecho)

    def _contains_(self, clave):
        return self._buscar(clave, self.raiz) is not None

    def _iter_(self):
        yield from self._inOrden(self.raiz)

    def _inOrden(self, nodo):
        if nodo is not None:
            yield from self._inOrden(nodo.hijoIzquierdo)
            yield (nodo.clave, nodo.cargaUtil)
            yield from self._inOrden(nodo.hijoDerecho)

    def _delitem_(self, clave):
        self.eliminar(clave)

    def eliminar(self, clave):
        nodo = self._buscar(clave, self.raiz)
        if nodo is None:
            raise Exception("Clave no encontrada")
        self._eliminarNodo(nodo)
        self.tamano -= 1

    def _encontrarSucesor(self, nodo):
        actual = nodo.hijoDerecho
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def _trasplantar(self, u, v):
        if u.esRaiz():
            self.raiz = v
        elif u.esHijoIzquierdo():
            u.padre.hijoIzquierdo = v
        else:
            u.padre.hijoDerecho = v
        if v is not None:
            v.padre = u.padre

    def _eliminarNodo(self, nodo):
        if nodo.esHoja():
            self._trasplantar(nodo, None)
        elif nodo.tieneHijoIzquierdo() and not nodo.tieneHijoDerecho():
            self._trasplantar(nodo, nodo.hijoIzquierdo)
        elif nodo.tieneHijoDerecho() and not nodo.tieneHijoIzquierdo():
            self._trasplantar(nodo, nodo.hijoDerecho)
        else:
            sucesor = self._encontrarSucesor(nodo)
            if sucesor.padre != nodo:
                self._trasplantar(sucesor, sucesor.hijoDerecho)
                sucesor.hijoDerecho = nodo.hijoDerecho
                if sucesor.hijoDerecho:
                    sucesor.hijoDerecho.padre = sucesor
            self._trasplantar(nodo, sucesor)
            sucesor.hijoIzquierdo = nodo.hijoIzquierdo
            if sucesor.hijoIzquierdo:
                sucesor.hijoIzquierdo.padre = sucesor

    def _len_(self):
        return self.tamano
