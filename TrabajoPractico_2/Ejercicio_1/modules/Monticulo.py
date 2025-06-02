class MonticuloBinario:
    def __init__(self):
        self.heap = []
        self.index = 0  # Para mantener el orden de llegada en caso de empate

    def insertar(self, paciente):
        self.heap.append((paciente.get_riesgo(), self.index, paciente))
        self.index += 1
        self.__subir(len(self.heap) - 1)

    def extraer(self):
        if self.esta_vacio():
            return None
        self.__intercambiar(0, len(self.heap) - 1)
        minimo = self.heap.pop()
        self.__bajar(0)
        return minimo[2]

    def esta_vacio(self):
        return len(self.heap) == 0

    def cantidad(self):
        return len(self.heap)

    def mostrar_pacientes(self):
        for _, _, paciente in self.heap:
            print('\t', paciente)

    def __subir(self, idx):
        padre = (idx - 1) // 2
        if padre >= 0 and self.heap[idx] < self.heap[padre]:
            self.__intercambiar(idx, padre)
            self.__subir(padre)

    def __bajar(self, idx):
        hijo_izq = 2 * idx + 1
        hijo_der = 2 * idx + 2
        menor = idx

        if hijo_izq < len(self.heap) and self.heap[hijo_izq] < self.heap[menor]:
            menor = hijo_izq
        if hijo_der < len(self.heap) and self.heap[hijo_der] < self.heap[menor]:
            menor = hijo_der

        if menor != idx:
            self.__intercambiar(idx, menor)
            self.__bajar(menor)

    def __intercambiar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
