import datetime
from modules.Monticulo import MonticuloBinario

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.tiempos_llegada = {}  # Diccionario: paciente -> hora de llegada

    def encolar(self, paciente):
        self.monticulo.insertar(paciente)
        self.tiempos_llegada[paciente] = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def desencolar(self):
        paciente = self.monticulo.extraer()
        if paciente is not None:
            self.tiempos_llegada.pop(paciente, None)
        return paciente

    def esta_vacia(self):
        return self.monticulo.esta_vacio()

    def cantidad(self):
        return self.monticulo.cantidad()

    def mostrar(self):
        print("Pacientes en espera (orden de atención):")
        pacientes_ordenados = sorted(self.monticulo.heap)
        for prioridad, orden, paciente in pacientes_ordenados:
            llegada = self.tiempos_llegada.get(paciente, "Hora desconocida")
            print(f"\t{paciente} -> {prioridad} | Llegada: {llegada}")

