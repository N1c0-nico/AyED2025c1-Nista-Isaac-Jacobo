# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

#FuncionDeCrearListasDeNumeros
def Crearlista (n):
    import random
    lista=[]
    for numero in range (n):
        numero = random.randint (10000,99999)
        lista.append(numero)
    return lista

#FuncionDeTomarTiempos
def Tiempos(Ordenador,tamanos):
    import time
    import random 
    aux=[]
    for n in tamanos:

        datos = [random.randint(1, 10000) for _ in range(n)]    

        inicio = time.perf_counter()
        Ordenador(datos.copy())
        fin = time.perf_counter()
        aux.append (fin - inicio)
    return aux