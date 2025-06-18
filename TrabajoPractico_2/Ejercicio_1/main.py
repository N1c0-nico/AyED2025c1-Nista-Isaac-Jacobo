import time
import datetime
import modules.paciente as pac
import random
from modules.ColaPrioridad import ColaDePrioridad  # Asumimos que guardaste esta clase en este archivo

# Simulación con la nueva cola de prioridad
n = 20  # cantidad de ciclos de simulación
cola_de_espera = ColaDePrioridad()  # Usamos la cola de prioridad

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    paciente = pac.Paciente()
    cola_de_espera.encolar(paciente)

    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        paciente_atendido = cola_de_espera.desencolar()
        print('*' * 40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*' * 40)
    else:
        pass

    print()
    print('Pacientes que faltan atenderse:', cola_de_espera.cantidad())
    cola_de_espera.mostrar()

    print()
    print('-*-' * 15)

    time.sleep(1)
