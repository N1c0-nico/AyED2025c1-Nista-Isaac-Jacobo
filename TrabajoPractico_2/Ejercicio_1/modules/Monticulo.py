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

# class MonticuloBinario:
#     def __init__(self):
#         self.listaMonticulo = [0]
#         self.tamanoActual = 0


#     def infiltArriba(self,i):
#       while i // 2 > 0:
#         if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
#           tmp = self.listaMonticulo[i // 2]
#           self.listaMonticulo[i // 2] = self.listaMonticulo[i]
#           self.listaMonticulo[i] = tmp
#           i = i // 2

#     def insertar(self,k):
#       self.listaMonticulo.append(k)
#       self.tamanoActual = self.tamanoActual + 1
#       self.infiltArriba(self.tamanoActual)

#     def infiltAbajo(self,i):
#       while (i * 2) <= self.tamanoActual:
#         hm = self.hijoMin(i)
#         if self.listaMonticulo[i] > self.listaMonticulo[hm]:
#           tmp = self.listaMonticulo[i]
#           self.listaMonticulo[i] = self.listaMonticulo[hm]
#           self.listaMonticulo[hm] = tmp
#         i = hm

#     def hijoMin(self,i):
#       if i * 2 + 1 > self.tamanoActual:
#           return i * 2
#       else:
#         if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
#             return i * 2
#         else:
#             return i * 2 + 1

#     def eliminarMin(self):
#       valorSacado = self.listaMonticulo[1]
#       self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
#       self.tamanoActual = self.tamanoActual - 1
#       self.listaMonticulo.pop()
#       self.infiltAbajo(1)
#       return valorSacado

#     def construirMonticulo(self,unaLista):
#       i = len(unaLista) // 2
#       self.tamanoActual = len(unaLista)
#       self.listaMonticulo = [0] + unaLista[:]
#       while (i > 0):
#         self.infiltAbajo(i)
#         i = i - 1

# miMonticulo = MonticuloBinario()
# miMonticulo.construirMonticulo([9,5,6,2,3])

# print(miMonticulo.eliminarMin())
# print(miMonticulo.eliminarMin())
# print(miMonticulo.eliminarMin())
# print(miMonticulo.eliminarMin())
# print(miMonticulo.eliminarMin())
