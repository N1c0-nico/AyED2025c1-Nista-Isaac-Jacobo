from modules.Monticulo import MonticuloBinario

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def encolar(self, paciente):
        riesgo = paciente.get_riesgo()
        tiempo = paciente.get_tiempo().timestamp()
        # Insertar una tupla (prioridad principal, secundaria, objeto)
        self.monticulo.insertar((riesgo, tiempo, paciente))

    def desencolar(self):
        if self.monticulo.tamanoActual == 0:
            return None
        return self.monticulo.eliminarMin()[2]
