class MonticuloBinario: # Definimos un montículo binario, que organiza elementos por prioridad
    def __init__(self):
        self.monticulo = [] # Creamos una Lista donde se almacenan las tuplas (distancia, aldea)

    def insertar(self, distancia, aldea): # Función para agregar una aldea al montículo
        self.monticulo.append((distancia, aldea))  # Agrega al final
        self.__subir(len(self.monticulo) - 1)       # Reorganiza hacia arriba para mantener el orden del montículo

    def extraer(self): # Función para extraer la aldea mas cercana a la raíz
        if self.esta_vacio():
            raise IndexError("El montículo está vacío")
        self.__intercambiar(0, len(self.monticulo) - 1)  # Mueve la aldea al final 
        distancia_aldea = self.monticulo.pop()           # Sacamos la aldea
        self.__bajar(0)                                  # Reorganiza hacia arriba para mantener el orden del montículo
        return distancia_aldea

    def esta_vacio(self):
        return len(self.monticulo) == 0

    def __subir(self, indice): # Función que reorganiza a las aldeas comparando su indice con el de su "padre", hasta que este deje de tener mas prioridad que éste
        while indice > 0:
            padre = (indice - 1) // 2  # Calcula la posición del "padre" del elemento

            if self.monticulo[indice][0] < self.monticulo[padre][0]: # Si existe el padre y el hijo tiene más prioridad
                self.__intercambiar(indice, padre) # Intercambia con el padre
                
                indice = padre
            else:
                break


    def __bajar(self, indice):  # Función que reorganiza a las aldeas, comparando su índice con el de sus hijos
        longitud = len(self.monticulo)
        while True:
            hijo_izq = 2 * indice + 1 # Calcula la posición del hijo izquierdo
            hijo_der = 2 * indice + 2  # Calcula la posición del hijo derecho
            menor = indice

            if hijo_izq < longitud and self.monticulo[hijo_izq][0] < self.monticulo[menor][0]:
                menor = hijo_izq
            if hijo_der < longitud and self.monticulo[hijo_der][0] < self.monticulo[menor][0]:
                menor = hijo_der

            if menor == indice:
                break

            self.__intercambiar(indice, menor)
            indice = menor


    def __intercambiar(self, i, j):  # Intercambia dos elementos en el montículo
        self.monticulo[i], self.monticulo[j] = self.monticulo[j], self.monticulo[i]

