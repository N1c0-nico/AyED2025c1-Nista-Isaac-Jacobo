class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if not nodo:
            return NodoAVL(clave, valor)
        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar(nodo.derecha, clave, valor)
        else:
            raise KeyError("La clave ya existe.")

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        return self._balancear(nodo)

    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo, clave):
        if not nodo:
            return nodo
        if clave < nodo.clave:
            nodo.izquierda = self._eliminar(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self._eliminar(nodo.derecha, clave)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            temp = self._min_nodo(nodo.derecha)
            nodo.clave, nodo.valor = temp.clave, temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.clave)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        return self._balancear(nodo)

    def obtener(self, clave):
        nodo = self.raiz
        while nodo:
            if clave == nodo.clave:
                return nodo.valor
            elif clave < nodo.clave:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        raise KeyError("Clave no encontrada")

    def en_rango(self, f1, f2):
        resultado = []
        self._en_rango(self.raiz, f1, f2, resultado)
        return resultado

    def _en_rango(self, nodo, f1, f2, resultado):
        if nodo:
            if f1 <= nodo.clave <= f2:
                resultado.append((nodo.clave, nodo.valor))
            if f1 < nodo.clave:
                self._en_rango(nodo.izquierda, f1, f2, resultado)
            if nodo.clave < f2:
                self._en_rango(nodo.derecha, f1, f2, resultado)

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _balancear(self, nodo):
        balance = self._balance(nodo)
        if balance > 1:
            if self._balance(nodo.izquierda) < 0:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1:
            if self._balance(nodo.derecha) > 0:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)
        return nodo

    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        x.altura = 1 + max(self._altura(x.izquierda), self._altura(x.derecha))
        return x

    def _rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = 1 + max(self._altura(x.izquierda), self._altura(x.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def _min_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual