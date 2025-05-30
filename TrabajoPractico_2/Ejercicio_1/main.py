import time
import datetime
import modules.paciente as pac
import random
from modules.Monticulo import MonticuloBinario

# Simulación con el montículo personalizado
n = 20  # cantidad de ciclos de simulación
cola_de_espera = MonticuloBinario()  # Usamos el montículo para gestionar los pacientes

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    paciente = pac.Paciente()
    cola_de_espera.insertar(paciente)

    if random.random() < 0.5 and not cola_de_espera.esta_vacio():
        paciente_atendido = cola_de_espera.extraer()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        pass

    print()
    print('Pacientes que faltan atenderse:', cola_de_espera.cantidad())
    cola_de_espera.mostrar_pacientes()

    print()
    print('-*-'*15)
    
    time.sleep(1)

# import time
# import datetime
# from modules.paciente import Paciente
# import random
# from modules.ColaPrioridad import ColaDePrioridad  # tu nueva clase

# n = 20  # cantidad de ciclos de simulación
# cola_prioritaria = ColaDePrioridad()

# for i in range(n):
#     ahora = datetime.datetime.now()
#     print('-*-' * 15)
#     print('\n', ahora.strftime('%d/%m/%Y %H:%M:%S'), '\n')

#     # Crear nuevo paciente con hora actual
#     paciente = Paciente(ahora)

#     if random.random() < 0.5 and not cola_prioritaria.esta_vacia():
#         # Se atiende el paciente más prioritario
#         paciente_atendido = cola_prioritaria.desencolar()
#         print('*' * 40)
#         print('Se atiende el paciente:', paciente_atendido)
#         print('*' * 40)
#     else:
#         # El nuevo paciente entra a la cola de espera
#         cola_prioritaria.encolar(paciente)

#     print()
#     print('Pacientes que faltan atenderse:', len(cola_prioritaria.pacientes_en_espera()))
#     for p in cola_prioritaria.pacientes_en_espera():
#         print('\t', p)

#     print()
#     print('-*-' * 15)

#     time.sleep(1)
