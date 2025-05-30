# # -*- coding: utf-8 -*-
# """
# Sala de emergencias
# """

import time
import datetime
import random
from modules.paciente import Paciente 
from modules.ColaPrioridad import ColaDePrioridad

cola_prioritaria = ColaDePrioridad()
n = 20  # ciclos de simulación

for i in range(n):
    ahora = datetime.datetime.now()
    print('-*-'*15)
    print('\n', ahora.strftime('%d/%m/%Y %H:%M:%S'), '\n')

    # Se crea paciente con hora actual
    paciente = Paciente(ahora)
    cola_prioritaria.encolar(paciente)

    # 50% de probabilidad de atender a alguien
    if random.random() < 0.5:
        paciente_atendido = cola_prioritaria.desencolar()
        if paciente_atendido:
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
        else:
            print("No hay pacientes para atender.")
    else:
        pass  # se sigue atendiendo paciente anterior

    print()
    print('Pacientes que faltan atenderse:', cola_prioritaria.monticulo.tamanoActual)
    for i in range(1, cola_prioritaria.monticulo.tamanoActual + 1):
        print('\t', cola_prioritaria.monticulo.listaMonticulo[i][2])

    print()
    print('-*-'*15)
    time.sleep(1)


# import time
# import datetime
# import modules.paciente as pac
# import random

# n = 20  # cantidad de ciclos de simulación

# cola_de_espera = list()

# # Ciclo que gestiona la simulación
# for i in range(n):
#     # Fecha y hora de entrada de un paciente
#     ahora = datetime.datetime.now()
#     fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
#     print('-*-'*15)
#     print('\n', fecha_y_hora, '\n')

#     # Se crea un paciente un paciente por segundo
#     # La criticidad del paciente es aleatoria
#     paciente = pac.Paciente()
#     cola_de_espera.append(paciente)

#     # Atención de paciente en este ciclo: en el 50% de los casos
#     if random.random() < 0.5:
#         # se atiende paciente que se encuentra al frente de la cola
#         paciente_atendido = cola_de_espera.pop(0)
#         print('*'*40)
#         print('Se atiende el paciente:', paciente_atendido)
#         print('*'*40)
#     else:
#         # se continúa atendiendo paciente de ciclo anterior
#         pass
    
#     print()

#     # Se muestran los pacientes restantes en la cola de espera
#     print('Pacientes que faltan atenderse:', len(cola_de_espera))
#     for paciente in cola_de_espera:
#         print('\t', paciente)
    
#     print()
#     print('-*-'*15)
    
#     time.sleep(1)
