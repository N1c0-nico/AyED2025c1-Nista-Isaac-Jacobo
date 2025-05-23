class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self, clave, valor=None):
        if valor is None:
            valor = clave  # Usamos la clave como valor si no se especifica
        if self.raiz is None:
            self.raiz = Nodo(clave, valor)
        else:
            self.raiz = self._insertar(self.raiz, clave, valor)
        self.tamano += 1

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            return Nodo(clave, valor)

        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._insertar(nodo.hijoIzquierdo, clave, valor)
            nodo.hijoIzquierdo.padre = nodo
        else:
            nodo.hijoDerecho = self._insertar(nodo.hijoDerecho, clave, valor)
            nodo.hijoDerecho.padre = nodo

        return self._balancear(nodo)

    def _altura(self, nodo):
        if nodo is None:
            return -1
        return max(self._altura(nodo.hijoIzquierdo), self._altura(nodo.hijoDerecho)) + 1

    def _factor_balance(self, nodo):
        return self._altura(nodo.hijoIzquierdo) - self._altura(nodo.hijoDerecho)

    def _balancear(self, nodo):
        balance = self._factor_balance(nodo)

        if balance > 1:
            if self._factor_balance(nodo.hijoIzquierdo) < 0:
                nodo.hijoIzquierdo = self._rotar_izquierda(nodo.hijoIzquierdo)
            return self._rotar_derecha(nodo)

        if balance < -1:
            if self._factor_balance(nodo.hijoDerecho) > 0:
                nodo.hijoDerecho = self._rotar_derecha(nodo.hijoDerecho)
            return self._rotar_izquierda(nodo)

        return nodo

    def _rotar_izquierda(self, z):
        y = z.hijoDerecho
        T2 = y.hijoIzquierdo

        y.hijoIzquierdo = z
        z.hijoDerecho = T2

        if T2:
            T2.padre = z
        y.padre = z.padre
        z.padre = y

        return y

    def _rotar_derecha(self, z):
        y = z.hijoIzquierdo
        T3 = y.hijoDerecho

        y.hijoDerecho = z
        z.hijoIzquierdo = T3

        if T3:
            T3.padre = z
        y.padre = z.padre
        z.padre = y

        return y

    def print_inorder(self):
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.hijoIzquierdo)
                print(nodo.clave, end=" ")
                _inorden(nodo.hijoDerecho)
        _inorden(self.raiz)
        print()

    def check_balance(self):
        def _check(nodo):
            if nodo is None:
                return True
            balance = abs(self._factor_balance(nodo))
            if balance > 1:
                return False
            return _check(nodo.hijoIzquierdo) and _check(nodo.hijoDerecho)

        return _check(self.raiz)

    def obtener_raiz(self):
        return self.raiz.clave if self.raiz else None
