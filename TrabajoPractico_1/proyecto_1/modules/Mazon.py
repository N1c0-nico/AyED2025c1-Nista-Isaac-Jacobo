
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from modules.ClaseNodoYLDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    """Excepción personalizada para indicar que el mazo está vacío."""
    pass

class Mazo:
    def _init_(self):
        self.cartas = ListaDobleEnlazada()

    def agregar_carta_al_final(self, carta):
        self.cartas.append(carta)

    def agregar_carta_al_inicio(self, carta):
        self.cartas.prepend(carta)

    def extraer_carta_del_final(self):
        if self.cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío. No se puede extraer una carta del final.")
        return self.cartas.pop()

    def extraer_carta_del_inicio(self):
        if self.cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío. No se puede extraer una carta del inicio.")
        return self.cartas.popleft()

    def _len_(self):
        """Devuelve la cantidad de cartas en el mazo."""
        return len(self.cartas)

    def _str_(self):
        """Devuelve una representación en cadena del mazo."""
        return " -> ".join(str(carta) for carta in self.cartas)