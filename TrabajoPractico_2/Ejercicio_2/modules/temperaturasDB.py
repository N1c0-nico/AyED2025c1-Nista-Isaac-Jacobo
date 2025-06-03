from datetime import datetime  # Importa la clase datetime para trabajar con fechas
from modules.ColaPrioridad import ColaDePrioridad  # Importa la clase ColaDePrioridad desde el módulo correspondiente

class Temperaturas_DB:
    def __init__(self):
        # Inicializa la base de datos creando una cola de prioridad para almacenar las temperaturas
        self.datos = ColaDePrioridad()

    def guardar_temperatura(self, temperatura, fecha_str):
        # Convierte la fecha en formato string a un objeto datetime
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        # Inserta la temperatura con la fecha como clave en la cola de prioridad (árbol)
        self.datos.encolar(fecha, temperatura)

    def devolver_temperatura(self, fecha_str):
        # Convierte la fecha string a objeto datetime
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        try:
            # Intenta obtener la temperatura almacenada para esa fecha
            return self.datos.obtener(fecha)
        except KeyError:
            # Si no existe la clave (fecha), devuelve None
            return None

    def cantidad_muestras(self): # Función que devuelve la cantidad total de temperaturas almacenadas (número de elementos en la cola)
        return self.datos.tamano

    def borrar_temperatura(self, fecha_str): # Función que convierte la fecha string a datetime
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.datos.desencolar(fecha) # Elimina la temperatura asociada a esa fecha de la cola de prioridad

    def max_temp_rango(self, f1_str, f2_str): # Función que convierte las fechas de inicio y fin del rango a objetos datetime
        f1 = datetime.strptime(f1_str, "%d/%m/%Y")
        f2 = datetime.strptime(f2_str, "%d/%m/%Y")
        # Busca la temperatura máxima entre las fechas del rango inclusive, devolviendo None si no hay datos
        return max(
            (valor for clave, valor in self.datos if f1 <= clave <= f2),
            default=None
        )

    def min_temp_rango(self, f1_str, f2_str): # Función que convierte las fechas de inicio y fin del rango a objetos datetime
        f1 = datetime.strptime(f1_str, "%d/%m/%Y")
        f2 = datetime.strptime(f2_str, "%d/%m/%Y")
        # Busca la temperatura mínima entre las fechas del rango inclusive, devolviendo None si no hay datos
        return min(
            (valor for clave, valor in self.datos if f1 <= clave <= f2),
            default=None
        )

    def temp_extremos_rango(self, f1_str, f2_str): # Función que devuelve una tupla con la temperatura mínima y máxima dentro del rango dado
        return (self.min_temp_rango(f1_str, f2_str),
                self.max_temp_rango(f1_str, f2_str))

    def devolver_temperaturas(self, f1_str, f2_str):
        # Convierte las fechas de inicio y fin del rango a objetos datetime
        f1 = datetime.strptime(f1_str, "%d/%m/%Y")
        f2 = datetime.strptime(f2_str, "%d/%m/%Y")
        # Crea una lista con strings que representan las temperaturas y fechas dentro del rango en formato legible
        resultado = [
            f"{clave.strftime('%d/%m/%Y')}: {valor} ºC"
            for clave, valor in self.datos
            if f1 <= clave <= f2
        ]
        # Devuelve la lista con las temperaturas y sus fechas
        return resultado
