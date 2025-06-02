# modules/monticulo.py
class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def insertar(self, tupla):
        self.listaMonticulo.append(tupla)
        self.tamanoActual += 1
        self.subir(self.tamanoActual)

    def subir(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = (
                    self.listaMonticulo[i // 2],
                    self.listaMonticulo[i],
                )
            i = i // 2

    def eliminarMin(self):
        if self.tamanoActual == 0:
            return None
        minimo = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual -= 1
        self.listaMonticulo.pop()
        self.bajar(1)
        return minimo

    def bajar(self, i):
        while (i * 2) <= self.tamanoActual:
            minHijo = self.hijo_minimo(i)
            if self.listaMonticulo[i] > self.listaMonticulo[minHijo]:
                self.listaMonticulo[i], self.listaMonticulo[minHijo] = (
                    self.listaMonticulo[minHijo],
                    self.listaMonticulo[i],
                )
            i = minHijo

    def hijo_minimo(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
