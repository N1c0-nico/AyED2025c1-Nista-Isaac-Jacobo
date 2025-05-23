# Clase que representa un nodo de la lista doblemente enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Guarda el dato en el nodo
        self.anterior = None  # Puntero al nodo anterior (al principio es None)
        self.siguiente = None  # Puntero al nodo siguiente (al principio es None)

# Clase que representa la lista doblemente enlazada
class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None  # Referencia al primer nodo
        self.ultimo = None  # Referencia al último nodo
        self._longitud = 0  # Contador de nodos

    def esta_vacia(self):
        return self._longitud == 0  # Retorna True si la lista está vacía

    def __len__(self):
        return self._longitud  # Permite usar len(lista)

    # Agrega un nodo al comienzo de la lista
    def agregar_al_inicio(self, item):
        nuevo = Nodo(item)  # Crea el nuevo nodo
        if self.esta_vacia():  # Si la lista está vacía
            self.primero = self.ultimo = nuevo  # El nuevo nodo es el único, entonces es el primero y el último
        else:
            nuevo.siguiente = self.primero  # El nuevo apunta al que era el primero
            self.primero.anterior = nuevo  # El anterior primero apunta hacia atrás al nuevo
            self.primero = nuevo  # El nuevo pasa a ser el primero
        self._longitud += 1  # Incrementamos la longitud

    # Agrega un nodo al final de la lista
    def agregar_al_final(self, item):
        nuevo = Nodo(item)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo  # Si la lista está vacía, es el único nodo
        else:
            nuevo.anterior = self.ultimo  # El nuevo apunta hacia atrás al que era el último
            self.ultimo.siguiente = nuevo  # El anterior último apunta hacia adelante al nuevo
            self.ultimo = nuevo  # El nuevo es ahora el último
        self._longitud += 1

    # Inserta un nodo en una posición dada
    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)  # Si no se da posición, se agrega al final
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
                actual = actual.siguiente  # Caminamos hasta la posición deseada
            anterior = actual.anterior
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self._longitud += 1

    # Extrae (elimina y retorna) el nodo de una posición dada
    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("Lista vacía")
        
        if posicion is None:
            posicion = self._longitud - 1  # Por defecto, extrae el último
        elif posicion < 0:
            posicion = self._longitud + posicion  # Soporte para índices negativos
            if posicion < 0:
                raise Exception("Posición inválida")
        
        if posicion < 0 or posicion >= self._longitud:
            raise Exception("Posición inválida")
        
        if posicion == 0:  # Extraer el primero
            nodo = self.primero
            self.primero = nodo.siguiente
            if self.primero:
                self.primero.anterior = None
            else:
                self.ultimo = None  # La lista quedó vacía
            self._longitud -= 1
            return nodo.dato
        elif posicion == self._longitud - 1:  # Extraer el último
            nodo = self.ultimo
            self.ultimo = nodo.anterior
            if self.ultimo:
                self.ultimo.siguiente = None
            else:
                self.primero = None
            self._longitud -= 1
            return nodo.dato
        else:  # Extraer un nodo intermedio
            actual = self.primero
            for _ in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self._longitud -= 1
            return actual.dato

    # Crea una copia (nueva lista con los mismos datos)
    def copiar(self):
        lista_copia = ListaDobleEnlazada()
        actual = self.primero
        while actual is not None:
            lista_copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return lista_copia

    # Invierte la lista (da vuelta las conexiones entre nodos)
    def invertir(self):
        actual = self.primero
        while actual is not None:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior  # Intercambia los punteros
            actual = actual.anterior  # Se mueve hacia adelante en el nuevo orden
        self.primero, self.ultimo = self.ultimo, self.primero  # Intercambia primero y último

    # Une esta lista con otra (sin modificar la otra)
    def concatenar(self, otra):
        copia = otra.copiar()  # Se trabaja con una copia para no afectar la lista original
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

    # Permite usar el operador + entre listas
    def __add__(self, otra):
        nueva = self.copiar()
        nueva.concatenar(otra)
        return nueva

    # Representación en texto de la lista (útil para print)
    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " <-> ".join(elementos) + "]"

    # Permite iterar sobre la lista con un for
    def __iter__(self):
        actual = self.primero
        while actual:
            yield actual.dato
            actual = actual.siguiente

# Ejemplo de uso
if __name__ == "__main__":
    l1 = ListaDobleEnlazada()
    for i in range(10):
        l1.agregar_al_final(i)  # Agrega del 0 al 9
    print(len(l1))  # Imprime la longitud (10)
    extraido = l1.extraer()  # Extrae el último elemento (9)
    print(len(l1))  # Imprime la nueva longitud (9)
