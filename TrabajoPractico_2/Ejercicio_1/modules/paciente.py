# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, tiempo_de_llegada):  # <-- Acepta la hora
        n = len(nombres)
        self.__nombre = nombres[randint(0, n - 1)]
        self.__apellido = apellidos[randint(0, n - 1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo - 1]
        self.__tiempo = tiempo_de_llegada  # <-- Guarda la hora como datetime

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_riesgo(self):
        return self.__riesgo

    def get_descripcion_riesgo(self):
        return self.__descripcion

    def get_tiempo(self):
        return self.__tiempo

    def __str__(self):
        hora_formateada = self.__tiempo.strftime('%H:%M:%S')
        cad = f"{self.__nombre} {self.__apellido:<10}\t -> {self.__riesgo}-{self.__descripcion} ({hora_formateada})"
        return cad
