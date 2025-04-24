# Clase que representa una caja que guarda un dato y sabe quién está antes y después
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Guardamos el dato
        self.anterior = None  # No hay nadie antes todavía
        self.siguiente = None  # No hay nadie después todavía

# Clase que representa la lista doblemente enlazada
class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None  # No hay primer elemento aún
        self.ultimo = None  # No hay último elemento aún
        self._longitud = 0  # La lista está vacía

    # Preguntamos si la lista está vacía
    def esta_vacia(self):
        return self._longitud == 0

    # Cuántos elementos hay en la lista
    def __len__(self):
        return self._longitud

    # Agrega una caja al comienzo
    def agregar_al_inicio(self, item):
        nuevo = Nodo(item)  # Creamos una nueva caja con el dato
        if self.esta_vacia():  # Si la lista está vacía...
            self.primero = self.ultimo = nuevo  # Esa caja es la única, es primera y última
        else:
            nuevo.siguiente = self.primero  # El nuevo apunta al que era primero
            self.primero.anterior = nuevo  # El viejo primero ahora sabe que hay alguien antes
            self.primero = nuevo  # Ahora el nuevo es el primero
        self._longitud += 1  # La lista creció

    # Agrega una caja al final
    def agregar_al_final(self, item):
        nuevo = Nodo(item)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo  # El nuevo sabe quién era el último
            self.ultimo.siguiente = nuevo  # El viejo último apunta al nuevo
            self.ultimo = nuevo  # El nuevo ahora es el último
        self._longitud += 1

    # Inserta una caja en cierta posición
    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)  # Si no dijeron posición, va al final
            return
        if posicion < 0 or posicion > self._longitud:
            raise IndexError("Posición fuera de rango.")
        if posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion == self._longitud:
            self.agregar_al_final(item)
        else:
            nuevo = Nodo(item)
            actual = self.primero
            for _ in range(posicion):
                actual = actual.siguiente  # Caminamos hasta la posición
            anterior = actual.anterior
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self._longitud += 1

    # Saca una caja de cierta posición y devuelve el dato
    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("La lista está vacía.")
        if posicion is None:
            posicion = self._longitud - 1  # Si no dijeron cuál, sacamos la última
        if posicion < 0 or posicion >= self._longitud:
            raise IndexError("Posición fuera de rango.")
        if posicion == 0:
            dato = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero:
                self.primero.anterior = None
            else:
                self.ultimo = None
        elif posicion == self._longitud - 1:
            dato = self.ultimo.dato
            self.ultimo = self.ultimo.anterior
            if self.ultimo:
                self.ultimo.siguiente = None
            else:
                self.primero = None
        else:
            actual = self.primero
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self._longitud -= 1
        return dato

    # Hace una copia de la lista
    def copiar(self):
        nueva = ListaDobleEnlazada()
        actual = self.primero
        while actual:
            nueva.agregar_al_final(actual.dato)  # Copiamos dato por dato
            actual = actual.siguiente
        return nueva

    # Invierte el orden de la lista
    def invertir(self):
        actual = self.primero
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior  # Damos vuelta las flechas
            actual = actual.anterior  # Seguimos caminando, ahora por el nuevo siguiente
        self.primero, self.ultimo = self.ultimo, self.primero  # Cambiamos quién es el primero y quién el último

    # Une esta lista con otra
    def concatenar(self, otra):
        copia = otra.copiar()  # Copiamos la otra para no modificarla
        if copia.esta_vacia():
            return
        if self.esta_vacia():
            self.primero = copia.primero
            self.ultimo = copia.ultimo
        else:
            self.ultimo.siguiente = copia.primero
            copia.primero.anterior = self.ultimo
            self.ultimo = copia.ultimo
        self._longitud += len(copia)

    # Permite sumar dos listas con el operador +
    def __add__(self, otra):
        nueva = self.copiar()
        nueva.concatenar(otra)
        return nueva

    # Para imprimir la lista como texto
    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " <-> ".join(elementos) + "]"
