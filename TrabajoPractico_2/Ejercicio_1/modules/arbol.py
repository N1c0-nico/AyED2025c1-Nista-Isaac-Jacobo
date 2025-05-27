class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None
        self.altura = 1  # <-- Nueva propiedad para balance AVL

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


class ArbolBinarioDB:
    def __init__(self):
        self.__raiz = None
        self.__tamano = 0

    @property
    def tamano(self):
        return self.__tamano
    
    @property
    def raiz(self):
        return self.__raiz


    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _actualizar_altura(self, nodo):
        nodo.altura = max(self._altura(nodo.hijoIzquierdo), self._altura(nodo.hijoDerecho)) + 1

    def _balance_factor(self, nodo):
        return self._altura(nodo.hijoIzquierdo) - self._altura(nodo.hijoDerecho)

    def _rotacion_derecha(self, y):
        x = y.hijoIzquierdo
        T2 = x.hijoDerecho

        x.hijoDerecho = y
        y.hijoIzquierdo = T2

        if T2:
            T2.padre = y
        x.padre = y.padre
        y.padre = x

        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    def _rotacion_izquierda(self, x):
        y = x.hijoDerecho
        T2 = y.hijoIzquierdo

        y.hijoIzquierdo = x
        x.hijoDerecho = T2

        if T2:
            T2.padre = x
        y.padre = x.padre
        x.padre = y

        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    def agregar(self, clave, valor):
        self.__raiz, nodo_insertado = self._agregar(clave, valor, self.__raiz)
        if self.__raiz:
            self.__raiz.padre = None
        if nodo_insertado is not None:
            self.__tamano += 1

    def _agregar(self, clave, valor, nodoActual):
        if nodoActual is None:
            return NodoArbol(clave, valor), NodoArbol(clave, valor)

        nodo_insertado = None

        if clave == nodoActual.clave:
            # Si clave ya existe, solo actualiza el valor, no agrega nodo nuevo
            nodoActual.cargaUtil = valor
            return nodoActual, None

        if clave < nodoActual.clave:
            nodoActual.hijoIzquierdo, nodo_insertado = self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            if nodoActual.hijoIzquierdo:
                nodoActual.hijoIzquierdo.padre = nodoActual
        else:
            nodoActual.hijoDerecho, nodo_insertado = self._agregar(clave, valor, nodoActual.hijoDerecho)
            if nodoActual.hijoDerecho:
                nodoActual.hijoDerecho.padre = nodoActual

        self._actualizar_altura(nodoActual)

        balance = self._balance_factor(nodoActual)

        # Caso Izquierda-Izquierda
        if balance > 1 and clave < nodoActual.hijoIzquierdo.clave:
            return self._rotacion_derecha(nodoActual), nodo_insertado

        # Caso Derecha-Derecha
        if balance < -1 and clave > nodoActual.hijoDerecho.clave:
            return self._rotacion_izquierda(nodoActual), nodo_insertado

        # Caso Izquierda-Derecha
        if balance > 1 and clave > nodoActual.hijoIzquierdo.clave:
            nodoActual.hijoIzquierdo = self._rotacion_izquierda(nodoActual.hijoIzquierdo)
            if nodoActual.hijoIzquierdo:
                nodoActual.hijoIzquierdo.padre = nodoActual
            return self._rotacion_derecha(nodoActual), nodo_insertado

        # Caso Derecha-Izquierda
        if balance < -1 and clave < nodoActual.hijoDerecho.clave:
            nodoActual.hijoDerecho = self._rotacion_derecha(nodoActual.hijoDerecho)
            if nodoActual.hijoDerecho:
                nodoActual.hijoDerecho.padre = nodoActual
            return self._rotacion_izquierda(nodoActual), nodo_insertado

        return nodoActual, nodo_insertado
    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    def __iter__(self):
        yield from self._recorrer_inorden(self.__raiz)

    def _recorrer_inorden(self, nodo):
        if nodo:
            yield from self._recorrer_inorden(nodo.hijoIzquierdo)
            yield (nodo.clave, nodo.cargaUtil)
            yield from self._recorrer_inorden(nodo.hijoDerecho)

    def __estabalanceado(self, nodo):
        if nodo is None:
            return True, 0

        balanceado_izq, altura_izq = self.__estabalanceado(nodo.hijoIzquierdo)
        balanceado_der, altura_der = self.__estabalanceado(nodo.hijoDerecho)

        balanceado_actual = (
            balanceado_izq and
            balanceado_der and
            abs(altura_izq - altura_der) <= 1
        )

        altura_actual = max(altura_izq, altura_der) + 1

        return balanceado_actual, altura_actual

    def esta_balanceado(self):
        balanceado, _ = self.__estabalanceado(self.__raiz)
        return balanceado

