class MonticuloBinario:
    def __init__(self):
        self.heap = []

    def insertar(self, prioridad, valor):
        self.heap.append((prioridad, valor))
        self.__subir(len(self.heap) - 1)

    def extraer(self):
        if self.esta_vacio():
            raise IndexError("El montículo está vacío")
        self.__intercambiar(0, len(self.heap) - 1)
        valor = self.heap.pop()
        self.__bajar(0)
        return valor

    def esta_vacio(self):
        return len(self.heap) == 0

    def __subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2
            if self.heap[indice][0] < self.heap[padre][0]:
                self.__intercambiar(indice, padre)
                indice = padre
            else:
                break

    def __bajar(self, indice):
        longitud = len(self.heap)
        while True:
            hijo_izq = 2 * indice + 1
            hijo_der = 2 * indice + 2
            menor = indice

            if hijo_izq < longitud and self.heap[hijo_izq][0] < self.heap[menor][0]:
                menor = hijo_izq
            if hijo_der < longitud and self.heap[hijo_der][0] < self.heap[menor][0]:
                menor = hijo_der

            if menor == indice:
                break

            self.__intercambiar(indice, menor)
            indice = menor

    def __intercambiar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
