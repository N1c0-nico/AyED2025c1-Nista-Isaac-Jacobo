# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
def Crearlista (n):
    import random
    lista=[]
    for numero in range (n):
        numero = random.randint (10000,99999)
        lista.append(numero)
    return lista

