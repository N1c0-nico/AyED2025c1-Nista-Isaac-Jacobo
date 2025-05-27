# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import modules.paciente as pac
import random

n = 20  # cantidad de ciclos de simulación
cola_de_espera = list()

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente con hora de llegada actual
    paciente = pac.Paciente(ahora)
    cola_de_espera.append(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5 and cola_de_espera:
        paciente_atendido = cola_de_espera.pop(0)
        print('*' * 40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*' * 40)

    print()

    # Ordenar la cola antes de mostrarla: primero por riesgo, luego por hora de llegada
    cola_de_espera = sorted(cola_de_espera, key=lambda p: (p.get_riesgo(), p.get_tiempo()))

    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)

    print()
    print('-*-' * 15)

    time.sleep(1)
