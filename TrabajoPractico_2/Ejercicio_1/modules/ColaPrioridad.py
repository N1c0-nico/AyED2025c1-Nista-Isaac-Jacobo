import datetime
from modules.Monticulo import MonticuloBinario

class ColaDePrioridad: 
    def __init__(self): # Utilizamos un constructor para inicializar la cola de prioridad
        self.monticulo = MonticuloBinario()
        self.tiempos_llegada = {}  # Diccionario: paciente -> hora de llegada

    def encolar(self, paciente): # Función para agregar un paciente a la cola de prioridad
        self.monticulo.insertar(paciente)
        self.tiempos_llegada[paciente] = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def desencolar(self): # Función para eliminar un paciente de la cola de prioridad
        paciente = self.monticulo.extraer()
        if paciente is not None:
            self.tiempos_llegada.pop(paciente, None)
        return paciente

    def esta_vacia(self): # Función para verificar si la cola de prioridad está vacía
        return self.monticulo.esta_vacio()

    def cantidad(self): # Función para obtener la cantidad de pacientes en la cola de prioridad
        return self.monticulo.cantidad()

    def mostrar(self): # Función para mostrar los pacientes en la cola de prioridad
        print("Pacientes en espera (orden de atención):")
        pacientes_ordenados = sorted(self.monticulo.heap)
        for prioridad, orden, paciente in pacientes_ordenados:
            llegada = self.tiempos_llegada.get(paciente, "Hora desconocida")
            print(f"\t{paciente} -> {prioridad} | Llegada: {llegada}")

