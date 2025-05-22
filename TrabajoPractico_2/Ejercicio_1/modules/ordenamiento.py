class ColaPrioridad:
    def __init__(self):
        self.items = []

    def agregar(self, clave, valor):
        """Inserta el elemento en la posición correcta según prioridad y orden de llegada."""
        nuevo = (clave, valor)

        # Si la lista está vacía, simplemente lo agregamos
        if not self.items:
            self.items.append(nuevo)
            return

        # Buscar posición donde insertar (orden ascendente)
        insertado = False
        for i in range(len(self.items)):
            if nuevo < self.items[i]:
                self.items.insert(i, nuevo)
                insertado = True
                break

        # Si es el de menor prioridad, va al final
        if not insertado:
            self.items.append(nuevo)
    def obtener(self, clave):
        # """Devuelve el valor asociado a la clave si existe, sino lanza una excepción."""
        for prioridad, dato in self.items:
            if prioridad == clave:
                return dato
        raise Exception(f"Clave {clave} no encontrada")

    def esta_vacia(self):
        return len(self.items) == 0

    def len(self):
        return len(self.items)

    def str(self):
        return "\n".join([str(elem[2]) for elem in self.items])