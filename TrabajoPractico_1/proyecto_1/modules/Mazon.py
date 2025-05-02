import sys
import os
# Agregamos al path la carpeta dos niveles arriba, para encontrar los módulos personalizados
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Importamos la clase ListaDobleEnlazada desde el módulo correspondiente
from modules.ClaseNodoYLDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

# Definimos una excepción personalizada para cuando el mazo está vacío
class DequeEmptyError(Exception):
    """Excepción personalizada para indicar que el mazo está vacío."""
    pass

# Clase que representa un mazo de cartas usando una lista doblemente enlazada
class Mazo:
    def _init_(self):  
        self.cartas = ListaDobleEnlazada()  # Inicializamos el mazo como una lista doblemente enlazada

    def agregar_carta_al_final(self, carta):
        self.cartas.append(carta)  # Agrega una carta al final del mazo

    def agregar_carta_al_inicio(self, carta):
        self.cartas.prepend(carta)  # Agrega una carta al inicio del mazo

    def extraer_carta_del_final(self):
        if self.cartas.esta_vacia():
            # Si el mazo está vacío, lanzamos una excepción personalizada
            raise DequeEmptyError("El mazo está vacío. No se puede extraer una carta del final.")
        return self.cartas.pop()  # Extrae y devuelve la última carta

    def extraer_carta_del_inicio(self):
        if self.cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío. No se puede extraer una carta del inicio.")
        return self.cartas.popleft()  # Extrae y devuelve la primera carta

    def _len_(self):  
        """Devuelve la cantidad de cartas en el mazo."""
        return len(self.cartas)

    def _str_(self):  
        """Devuelve una representación en cadena del mazo."""
        return " -> ".join(str(carta) for carta in self.cartas)
