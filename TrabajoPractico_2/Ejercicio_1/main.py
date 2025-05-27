# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import modules.paciente as pac
import modules.arbol as ord
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = list()

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente con la hora actual
    paciente = pac.Paciente(ahora)
    cola_de_espera.append(paciente)

    # 50% de chance de atender al primer paciente en cola
    if random.random() < 0.5 and cola_de_espera:
        paciente_atendido = cola_de_espera.pop(0)
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        pass

    print()

    # Ordenar cola usando árbol binario
    arbol = ord.ArbolBinarioDB()
    for paciente in cola_de_espera:
        riesgo = paciente.get_riesgo()
        tiempo = paciente.get_tiempo().timestamp()
        clave = (riesgo, tiempo)
        arbol[clave] = paciente

    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for clave, paciente in arbol:
        print('\t', paciente)

    print()
    print('-*-'*15)
    time.sleep(1)

if arbol.esta_balanceado():
    print("El árbol está balanceado.")
else:
    print("El árbol NO está balanceado.")