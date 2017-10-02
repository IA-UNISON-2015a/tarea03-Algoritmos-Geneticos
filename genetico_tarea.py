#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
genetico_tarea.py
-----------------

En este módulo vas a desarrollar tu propio algoritmo
genético para resolver problemas de permutaciones

"""

import random
import genetico
from operator import itemgetter

__author__ = 'Rafael Castillo'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población, n_reemplazos, prob_muta, costo_min, costo_max, torneos_k=2):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """

        self.n_reemplazos = n_reemplazos
        self.prob_muta = prob_muta
        self.costo_min = costo_min
        self.costo_max = costo_max
        self.nombre = 'propuesto por Rafael Castillo'
        self.n_población = n_población
        self.torneos_k = torneos_k

        super().__init__(problema, n_población)
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        #



    @staticmethod
    def estado_a_cadena(estado):
        """
        Convierte un estado a una cadena de cromosomas independiente
        del problema de permutación

        @param estado: Una tupla con un estado
        @return: Una lista con una cadena de caracteres

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        """ La verdad no se me ocurrio que ponerle """
        return list(estado)

    @staticmethod
    def cadena_a_estado(cadena):
        """
        Convierte una cadena de cromosomas a un estado donde el estado es
        una posible solución a un problema de permutaciones

        @param cadena: Una lista de cromosomas o valores
        @return: Una tupla con un estado válido

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        """ igual aqui """
        return tuple(cadena)


    def adaptación(self, individuo):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado
        mejor, mayor costo, menor adaptción.

        @param individuo: Una lista de cromosomas
        @return un número con la adaptación del individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        """
        Si conocemos el costo minimo y maximo, podemos distribuir la
        adaptacion mas equitativamente
        """

        estado = self.cadena_a_estado(individuo)
        costo = self.problema.costo(estado)
        return 1 - (costo - self.costo_min) / (self.costo_max - self.costo_min)

    def torneos(self):
        return max((random.randint(0, len(self.población) - 1) for _ in range(self.torneos_k)),
            key=lambda i: self.población[i][0])

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        return list(zip((self.torneos() for _ in range(self.n_población)),
                        (self.torneos() for _ in range(self.n_población))))

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #

        # Detectar ciclos
        ciclos = []
        procesados = [False] * len(cadena1)  # indices procesados
        for i in range(len(cadena1)):
            if not procesados[i]:
                inicio_ciclo = i
                ciclo = [i]
                procesados[i] = True
                sig = cadena1.index(cadena2[i])
                while sig != inicio_ciclo:
                    ciclo.append(sig)
                    procesados[sig] = True
                    sig = cadena1.index(cadena2[sig])
                ciclos.append(ciclo)

        nueva_cadena = [0] * len(cadena1)
        alternancia = True
        for ciclo in ciclos:
            cadena = cadena1 if alternancia else cadena2
            for i in ciclo:
                nueva_cadena[i] = cadena[i]
            alternancia = not alternancia

        return nueva_cadena

    def mutación(self, individuos):
        """

        @param población: Una lista de individuos (listas).

        @return: None, es efecto colateral mutando los individuos
                 en la misma lista

        """
        ###################################################################
        #                          10 PUNTOS
        ###################################################################
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        """
        si tengo que mutar, agarro los primeros k elementos de un individuo
        y los pongo al final
        """
        for individuo in individuos:
            if random.random() < self.prob_muta:
                k = random.randint(0, len(individuo) - 1)
                # tengo que hacer esto porque no puedo mutar...
                for i in range(k):
                    x = individuo.pop(0)
                    individuo.append(x)


    def reemplazo_generacional(self, individuos):
        """
        Realiza el reemplazo generacional diferente al elitismo

        @param individuos: Una lista de cromosomas de hijos que pueden
                           usarse en el reemplazo
        @return: None (todo lo cambia internamente)

        Por default usamos solo el elitismo de conservar al mejor, solo si es
        mejor que lo que hemos encontrado hasta el momento.

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        """
        Reemplaza n individuos de la generacion al azar
        """
        reemplazo = [(self.adaptación(individuo), individuo)
                     for individuo in individuos][:self.n_reemplazos]
        reemplazo.append(max(self.población))
        random.shuffle(self.población)
        reemplazo = reemplazo + self.población
        self.población = reemplazo[:self.n_población]


if __name__ == "__main__":
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10, 5, 0.01, 1, 19)
    genetico.prueba(g_propio)
