from datetime import datetime
from modules.arbolAVL import ArbolBinarioBusqueda
class Temperaturas_DB:
    def __init__(self):
        self.datos = ArbolBinarioBusqueda()

    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.datos.insertar(fecha, temperatura)

    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        try:
            return self.datos.buscar(fecha)
        except KeyError:
            return None

    def cantidad_muestras(self): 
        return self.datos.tamano

    def borrar_temperatura(self, fecha_str): 
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.datos.eliminar(fecha) 

    def max_temp_rango(self, f1_str, f2_str): 
        f1 = datetime.strptime(f1_str, "%d/%m/%Y")
        f2 = datetime.strptime(f2_str, "%d/%m/%Y")
        return max(
            (valor for clave, valor in self.datos if f1 <= clave <= f2),
            default=None
        )

    def min_temp_rango(self, f1_str, f2_str): 
        f1 = datetime.strptime(f1_str, "%d/%m/%Y")
        f2 = datetime.strptime(f2_str, "%d/%m/%Y")
        return min(
            (valor for clave, valor in self.datos if f1 <= clave <= f2),
            default=None
        )

    def temp_extremos_rango(self, f1_str, f2_str): 
        return (self.min_temp_rango(f1_str, f2_str),
                self.max_temp_rango(f1_str, f2_str))

    def devolver_temperaturas(self, f1_str, f2_str):
        f1 = datetime.strptime(f1_str, "%d/%m/%Y")
        f2 = datetime.strptime(f2_str, "%d/%m/%Y")
        resultado = [
            f"{clave.strftime('%d/%m/%Y')}: {valor} ºC"
            for clave, valor in self.datos
            if f1 <= clave <= f2
        ]
        return resultado
