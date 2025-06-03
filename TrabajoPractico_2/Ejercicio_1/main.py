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