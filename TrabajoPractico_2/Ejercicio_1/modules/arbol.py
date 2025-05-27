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
    
    
    #Las siguientes funciones fueron agregadas para que nuestro código pase el test
    

    def obtener(self, clave):
        nodo = self._obtener_nodo(clave, self.__raiz)
        if nodo is None:
            raise KeyError(f"Clave no encontrada: {clave}")
        return nodo.cargaUtil

    def _obtener_nodo(self, clave, nodoActual):
        if nodoActual is None:
            return None
        if clave == nodoActual.clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener_nodo(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener_nodo(clave, nodoActual.hijoDerecho)
    def __contains__(self, clave):
        return self._obtener_nodo(clave, self.__raiz) is not None
    def eliminar(self, clave):
        self.__raiz = self._eliminar(self.__raiz, clave)
        if self.__raiz:
            self.__raiz.padre = None

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return None

        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._eliminar(nodo.hijoIzquierdo, clave)
            if nodo.hijoIzquierdo:
                nodo.hijoIzquierdo.padre = nodo
        elif clave > nodo.clave:
            nodo.hijoDerecho = self._eliminar(nodo.hijoDerecho, clave)
            if nodo.hijoDerecho:
                nodo.hijoDerecho.padre = nodo
        else:
            # Caso 1: Sin hijos
            if nodo.hijoIzquierdo is None and nodo.hijoDerecho is None:
                self.__tamano -= 1
                return None
            # Caso 2: Un solo hijo
            elif nodo.hijoIzquierdo is None:
                temp = nodo.hijoDerecho
                temp.padre = nodo.padre
                self.__tamano -= 1
                return temp
            elif nodo.hijoDerecho is None:
                temp = nodo.hijoIzquierdo
                temp.padre = nodo.padre
                self.__tamano -= 1
                return temp
            # Caso 3: Dos hijos
            else:
                sucesor = self._minimo(nodo.hijoDerecho)
                nodo.clave, nodo.cargaUtil = sucesor.clave, sucesor.cargaUtil
                nodo.hijoDerecho = self._eliminar(nodo.hijoDerecho, sucesor.clave)
                if nodo.hijoDerecho:
                    nodo.hijoDerecho.padre = nodo

        self._actualizar_altura(nodo)

        # Rebalanceo AVL
        balance = self._balance_factor(nodo)

        if balance > 1 and self._balance_factor(nodo.hijoIzquierdo) >= 0:
            return self._rotacion_derecha(nodo)
        if balance > 1 and self._balance_factor(nodo.hijoIzquierdo) < 0:
            nodo.hijoIzquierdo = self._rotacion_izquierda(nodo.hijoIzquierdo)
            return self._rotacion_derecha(nodo)
        if balance < -1 and self._balance_factor(nodo.hijoDerecho) <= 0:
            return self._rotacion_izquierda(nodo)
        if balance < -1 and self._balance_factor(nodo.hijoDerecho) > 0:
            nodo.hijoDerecho = self._rotacion_derecha(nodo.hijoDerecho)
            return self._rotacion_izquierda(nodo)

        return nodo

    def _minimo(self, nodo):
        actual = nodo
        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo
        return actual
