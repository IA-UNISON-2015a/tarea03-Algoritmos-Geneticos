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
import itertools
__author__ = 'Bárbara Galindo'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población, prob_muta=0.01):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'propuesto por el alumno'
        self.miPoblacion = []
        self.prob_muta = prob_muta
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
        return list(estado)
        #  raise NotImplementedError("¡Este metodo debe ser implementado!")

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
        return tuple(cadena)
        #  raise NotImplementedError("¡Este metodo debe ser implementado!")

        
    def adaptación(self, individuo):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado
        mejor, mayor costo, menor adaptación.

        @param individuo: Una lista de cromosomas
        @return un número con la adaptación del individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        return self.problema.costo(self.estado_a_cadena(individuo))
        #  raise NotImplementedError("¡Este metodo debe ser implementado!")

    def individuo_aleatorio(self, poblacion):
        return poblacion[random.randrange(len(poblacion))]

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        # miPoblacion = self.población[:]
        auxPoblacionIndices = []
        xd = []
        for x in range(len(self.población)):
            indice1 = random.randint(0, len(self.población) - 1)
            indice2 = random.randint(0, len(self.población) - 1)
            if indice1 == indice2:
                indice2 =+ random.randint(0, len(self.población) - 1)
            if self.población[indice1][0] > self.población[indice2][0]:
                auxPoblacionIndices.append(indice1)
            else:
                auxPoblacionIndices.append(indice2)
        for x in range(1, len(auxPoblacionIndices)):
            xd.append([auxPoblacionIndices[x - 1], auxPoblacionIndices[x]])
        return xd

        #  raise NotImplementedError("¡Este metodo debe ser implementado!")

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        
        hijo = []
        for x in range(len(cadena1)):
            if cadena1[x] not in hijo and cadena2[x] not in hijo:
                if random.random() > 0.5:
                    hijo.append(cadena1[x])
                else:
                    hijo.append(cadena2[x])
            else:
                if random.random() > 0.5:
                    for i in range(x):
                        if cadena1[i] not in hijo:
                            hijo.append(cadena1[x])
                else:
                    for i in range(x):
                        if cadena2[i] not in hijo:
                            hijo.append(cadena2[x])

        return hijo
        #raise NotImplementedError("¡Este metodo debe ser implementado!")

    def mutación(self, individuos):
        """

        @param poblacion: Una lista de individuos (listas).

        @return: None, es efecto colateral mutando los individuos
                 en la misma lista

        """
        ###################################################################
        #                          10 PUNTOS
        ###################################################################
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        for individuo in individuos:
            if random.random() < self.prob_muta:
                [individuo[i ^ 1] for i in range(len(individuo))]
        #raise NotImplementedError("¡Este metodo debe ser implementado!")

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
        for x in range(len(individuos)):
            if random.random() < 0.5:
                self.población[x] = (self.adaptación(individuos[x]), individuos[x])

if __name__ == "__main__":
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    genetico.prueba(g_propio)
