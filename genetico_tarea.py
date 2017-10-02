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

__author__ = 'Abraham Moreno'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población, prob_mut=0.01, prob_cruce=0.5):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'propuesto por el alumno'
        super().__init__(problema, n_población)
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        self.prob_mut = prob_mut
        self.prob_cruce = prob_cruce


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
        return 1 / (1.0 + self.problema.costo(self.cadena_a_estado(individuo)))
    
    @staticmethod
    def torneo(poblacion):
        """
        Regresa un indice de la lista poblacion.

        @param población: Una lista de  tuplas (aptitud, individuo)
        @return: El inidce del individuo seleccionado mediante el torneo

        """
        i = random.randint(0, len(poblacion)-1)
        j = random.randint(0, len(poblacion)-1)

        return i if poblacion[i][0] > poblacion[j][0] else j

    def selección_individual(self):
        """
        

        @return: Una tupla con los pares a unirse

        """
        i = self.torneo(self.población)
        j = self.torneo(self.población[:i] + self.población[i+1:])
        return i, j

    def selección(self):
        """
        Seleccion de estados mediante método de toreno

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        return [self.selección_individual()
                for _ in range(self.n_población)]

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        
        if random.random() < self.prob_cruce:
            return cadena1 if random.random() < 0.5 else cadena2
        else:
            length = (len(cadena1))
            corte1 = random.randint(0, length-1)
            corte2 = random.randint(corte1, length)
            hijo = cadena1[:corte1] + cadena2[corte1:corte2] + cadena1[corte2:]
            return hijo


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
        for ind in individuos:
            if random.random() < self.prob_mut:
                j, k = random.randint(0, len(ind)-1), random.randint(0, len(ind)-1)
                ind[j], ind[k] = ind[k], ind[j]


    def reemplazo_generacional(self, individuos):
        """
        Realiza el reemplazo generacional diferente al elitismo

        @param individuos: Una lista de cromosomas de hijos que pueden
                           usarse en el reemplazo
        @return: None (todo lo cambia internamente)


        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        reemplazo = [(self.adaptación(individuo), individuo)
                     for individuo in individuos]
        
        self.población = reemplazo[:self.n_población]


if __name__ == "__main__":
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    genetico.prueba(g_propio)
