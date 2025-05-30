from modules.Monticulo import MonticuloBinario
class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def encolar(self, paciente):
        # Menor riesgo tiene más prioridad: (1, hora)
        clave = (paciente.get_riesgo(), paciente.get_tiempo(), paciente)
        self.monticulo.insertar(clave)

    def desencolar(self):
        if self.monticulo.tamanoActual == 0:
            return None
        return self.monticulo.eliminarMin()[2]  # Solo devolver el paciente

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0

    def pacientes_en_espera(self):
        return [self.monticulo.listaMonticulo[i][2] for i in range(1, self.monticulo.tamanoActual + 1)]
