from modules2.temperaturasDB import TemperaturasDB

def test_base_datos_temperaturas():
    bd = TemperaturasDB()

    # Carga de datos de prueba
    bd.guardar_temperatura(7.0, "10/05/2025")
    bd.guardar_temperatura(10.7, "11/05/2025")
    bd.guardar_temperatura(3.5, "12/05/2025")
    bd.guardar_temperatura(13.9, "13/05/2025")
    bd.guardar_temperatura(17.1, "14/05/2025")
    bd.guardar_temperatura(22.3, "15/05/2025")
    bd.guardar_temperatura(20.0, "16/05/2025")
    bd.guardar_temperatura(17.0, "17/05/2025")
    bd.guardar_temperatura(15.2, "18/05/2025")
    bd.guardar_temperatura(10.3, "19/05/2025")
    bd.guardar_temperatura(12.7, "20/05/2025")

    # Verificar cantidad total
    assert bd.cantidad_muestras() == 11, "Fallo en cantidad_muestras()"

    # Recuperación individual por fecha
    assert bd.devolver_temperatura("11/05/2025") == 10.7, "Fallo en devolver_temperatura para 11/05/2025"
    assert bd.devolver_temperatura("14/05/2025") == 17.1, "Fallo en devolver_temperatura para 14/05/2025"
    assert bd.devolver_temperatura("18/05/2025") == 15.2, "Fallo en devolver_temperatura para 11/05/2025"

    # Máximo en rango
    assert bd.max_temp_rango("10/05/2025", "20/05/2025") == 22.3, "Fallo en max_temp_rango del 10 al 14/05"

    # Mínimo en rango
    assert bd.min_temp_rango("10/05/2025", "20/05/2025") == 3.5, "Fallo en min_temp_rango del 10 al 15/05"

    # Extremos dentro de un intervalo
    temp_min, temp_max = bd.temp_extremos_rango("10/05/2025", "20/05/2025")
    assert temp_min == 3.5 and temp_max == 22.3, "Fallo en temp_extremos_rango del 10 al 14/05"

    # Listado de temperaturas en rango
    esperado_rango = [
        "10/05/2025: 7.0 ºC",
        "11/05/2025: 10.7 ºC",
        "12/05/2025: 3.5 ºC",
        "13/05/2025: 13.9 ºC",
        "14/05/2025: 17.1 ºC",
        "15/05/2025: 22.3 ºC",
        "16/05/2025: 20.0 ºC",
        "17/05/2025: 17.0 ºC",
        "18/05/2025: 15.2 ºC",
        "19/05/2025: 10.3 ºC",
        "20/05/2025: 12.7 ºC"
    ]
    assert bd.devolver_temperaturas("10/05/2025", "20/05/2025") == esperado_rango, "Fallo en devolver_temperaturas del 10 al 14/05"

    # Eliminar registro específico
    bd.borrar_temperatura("12/05/2025")
    assert bd.cantidad_muestras() == 5, "Fallo en cantidad luego de borrar"
    assert bd.devolver_temperatura("12/05/2025") is None, "Fallo al verificar ausencia de dato eliminado"

    # Verificación posterior al borrado
    esperado_post_borrado = [
        "10/05/2025: 7.0 ºC",
        "11/05/2025: 10.7 ºC",
        "13/05/2025: 13.9 ºC",
        "14/05/2025: 17.1 ºC",
        "15/05/2025: 22.3 ºC",
        "16/05/2025: 20.0 ºC",
        "17/05/2025: 17.0 ºC",
        "18/05/2025: 15.2 ºC",
        "19/05/2025: 10.3 ºC",
        "20/05/2025: 12.7 ºC"
    ]
    assert bd.devolver_temperaturas("10/05/2025", "20/05/2025") == esperado_post_borrado, "Fallo en resultados tras eliminar temperatura del 12/05"

    print("¡Todas las validaciones se realizaron con éxito!")

# Ejecutar las pruebas
test_base_datos_temperaturas()
print("Solo los genios hacen eso, tenés que cerrar Python")
