from modules.monticulo import MonticuloBinario

class ColaDePrioridad:  # Definimos nuestra clase ColaDePrioridad
    def __init__(self):  # Definimos las caracteristicas de nuestra clase con el constructor "__init__"
        self.monticulo = MonticuloBinario()  # Crea un montículo binario (estructura para ordenar por prioridad)
        self.mapa = {}  # Diccionario que guarda los elementos por su clave
        self.tamano = 0  # Guarda cuántos elementos hay en total

    def encolar(self, clave, valor):  # Agrega un nuevo elemento con una clave y un valor
        if clave in self.mapa:  # Si la clave ya existe
            raise KeyError("La clave ya existe.")  # Lanza un error porque no se permiten claves repetidas
        self.mapa[clave] = valor  # Guarda el valor en el diccionario usando la clave
        self.monticulo.insertar((clave, valor))  # Inserta la tupla (clave, valor) en el montículo
        self.tamano += 1  # Aumenta el contador de elementos

    def desencolar(self, clave):  # Elimina un elemento usando su clave
        if clave not in self.mapa:  # Si la clave no existe, no hace nada
            return  
        del self.mapa[clave]  # Elimina la clave del diccionario
        self.tamano -= 1  # Disminuye el contador de elementos
        # No se elimina directamente del montículo: se ignora en lecturas
        # (esto significa que el montículo sigue teniendo el elemento, pero ya no se usa)

    def obtener(self, clave):  # Busca un valor usando su clave
        return self.mapa[clave]  # Devuelve el valor asociado a esa clave

    def __iter__(self):  # Permite recorrer los elementos de la cola
        # Devuelve un recorrido de la tupla (clave, valor) ordenados por clave
        return iter(sorted(self.mapa.items()))  # Ordena los elementos por clave y permite iterarlos (uno por uno)
