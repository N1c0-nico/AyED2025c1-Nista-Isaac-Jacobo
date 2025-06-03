class MonticuloBinario:  # Definimos un montículo binario, que organiza elementos por prioridad
    def __init__(self):  # Mediante el constructor "__init__", le damos caracteristicas al monticulo
        self.heap = []  # Lista donde se guardan los elementos (en forma de árbol)
        self.index = 0  # Un contador que define el orden de llegada

    def insertar(self, paciente):  # Función para agregar un paciente al montículo
        # Agrega una tupla con el riesgo del paciente, el orden de llegada y el paciente 
        self.heap.append((paciente.get_riesgo(), self.index, paciente))
        self.index += 1  # Aumenta el contador para el siguiente paciente
        self.__subir(len(self.heap) - 1)  # Reorganiza hacia arriba para mantener el orden del montículo

    def extraer(self):  # Función para extraer el paciente con mayor prioridad (el de más riesgo, o el que llegó antes en caso de que tengan el mismo riesgo)
        if   self.esta_vacio():  # Si el montículo está vacío, no hace nada
            return None  
        self.__intercambiar(0, len(self.heap) - 1)  # Intercambia el primero (el más prioritario) con el último en llegar
        minimo = self.heap.pop()  # Saca el último (que era el más prioritario)
        self.__bajar(0)  # Reorganiza el montículo hacia abajo
        return minimo[2]  # Devuelve el objeto paciente, no el riesgo ni el índice

    def esta_vacio(self):  # Función que Verifica si el montículo está vacío
        return len(self.heap) == 0  # Devuelve True si no hay elementos

    def cantidad(self):  # Función que devuelve cuántos pacientes hay
        return len(self.heap)

    def mostrar_pacientes(self):  # Función que muestra todos los pacientes en el montículo
        for _, _, paciente in self.heap:  # Recorre la lista y solo toma el paciente
            print('\t', paciente)  # Mostramos en terminal los pacientes en el montículo

    def __subir(self, idx):  # Función que reorganiza a los pacientes comparando su indice con el de su "padre", hasta que este deje de tener mas prioridad que éste
        padre = (idx - 1) // 2  # Calcula la posición del "padre" del elemento
        if padre >= 0 and self.heap[idx] < self.heap[padre]:  # Si existe el padre y el hijo tiene más prioridad
            self.__intercambiar(idx, padre)  # Intercambia con el padre
            self.__subir(padre)  # Repite el proceso con el padre

    def __bajar(self, idx):  # Función que reorganiza a los pacientes, comparando su índice con el de sus hijos
        hijo_izq = 2 * idx + 1  # Calcula la posición del hijo izquierdo
        hijo_der = 2 * idx + 2  # Calcula la posición del hijo derecho
        menor = idx  # Por defecto, el menor es el actual

        if hijo_izq < len(self.heap) and self.heap[hijo_izq] < self.heap[menor]:  # Si el hijo izq tiene más prioridad
            menor = hijo_izq
        if hijo_der < len(self.heap) and self.heap[hijo_der] < self.heap[menor]:  # Si el hijo der tiene aún más prioridad
            menor = hijo_der

        if menor != idx:  # Si alguno de los hijos tiene más prioridad
            self.__intercambiar(idx, menor)  # Intercambia con el que tenga más prioridad
            self.__bajar(menor)  # Repite el proceso con la nueva posición

    def __intercambiar(self, i, j):  # Intercambia dos elementos en el montículo
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]  # Intercambia las posiciones i y j
