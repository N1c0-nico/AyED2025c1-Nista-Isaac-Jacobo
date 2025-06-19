from modules.monticules import MonticuloBinario 

class ColaDePrioridad:
    def __init__(self): # Utilizamos un constructor para inicializar la cola de prioridad
        self.monticulo = MonticuloBinario()

    def encolar(self, prioridad, aldea): # Función para agregar aldeas a la cola de prioridad 
        #Además les asigna una prioridad basada en la distancia
        
        self.monticulo.insertar(prioridad, aldea)

    def desencolar(self): # Función que extrae la aldea con mayor prioridad (menor distancia) del montículo.

        return self.monticulo.extraer()

    def esta_vacio(self): # Función que verifica si la cola de prioridad está vacía.

        return self.monticulo.esta_vacio()

    def cantidad(self): #Función que devuelve la cantidad de aldeas en la cola de prioridad.
    
        return len(self.monticulo.monticulo)

    def mostrar(self): # Función que muestra las aldeas en espera, ordenadas por prioridad.
        
        print("Aldeas en espera (por prioridad de entrega):")
        aldeas_ordenadas = sorted(self.monticulo.monticulo)  # Ordenamos la lista para mostrarla más legible
        for prioridad, aldea in aldeas_ordenadas:
            print(f"\t{aldea} -> prioridad: {prioridad}")
