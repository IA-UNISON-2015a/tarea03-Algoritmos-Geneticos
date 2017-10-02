#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
genetico_tarea.py
-----------------

En este módulo vas a desarrollar tu propio algoritmo
genético para resolver problemas de permutaciones

"""

import random
from math import exp
import genetico

__author__ = 'AthenaVianney'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población, prob_mutacion = 0.0099):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'propuesto por el alumno'
        super().__init__(problema, n_población) #problema, n_poblacion, poblacion
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        #
        self.prob_mutacion = prob_mutacion
        

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
        #raise NotImplementedError("¡Este metodo debe ser implementado!")
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
        #raise NotImplementedError("¡Este metodo debe ser implementado!")
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
        #raise NotImplementedError("¡Este metodo debe ser implementado!")
        return exp(-self.problema.costo(self.cadena_a_estado(individuo)))

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar
        TORNEO
        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        #raise NotImplementedError("¡Este metodo debe ser implementado!")
        individuos = []
        for _ in range(len(self.población)-1):
            x1 = random.randint(0,len(self.población)-1)
            x2 = random.randint(0,len(self.población)-1)
            y1 = random.randint(0,len(self.población)-1)
            y2 = random.randint(0,len(self.población)-1)
            
            individuos.append((x1 if self.población[x1][0] > self.población[x2][0] else x2,
                               y1 if self.población[y1][0] > self.población[y2][0] else y2))
        return individuos

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        #raise NotImplementedError("¡Este metodo debe ser implementado!")
        child = []
        aux = list(range(0,len(cadena1)))
        for _ in range(len(cadena1)):
            ran = random.random()
            if ran < 0.5 and cadena1[_] in aux:
                child.append(cadena1[_])
                aux.remove(cadena1[_])
            elif cadena2[_] in aux:
                child.append(cadena2[_])
                aux.remove(cadena2[_])
            else:
                child.append(random.choice(aux))
        return child



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
        #raise NotImplementedError("¡Este metodo debe ser implementado!")
        for individuo in individuos:
            for i in range(len(individuo)):
                if random.random() < self.prob_mutacion:
                    j = individuo[i]
                    individuo[i], individuo[j] = individuo[j], individuo[i]
        return individuos

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
        reemplazo = [(self.adaptación(individuo), individuo)
                     for individuo in individuos]
        reemplazo.append(max(self.población))
        reemplazo.sort(reverse=True)
        self.población = reemplazo[:self.n_población]


if __name__ == "__main__":
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    genetico.prueba(g_propio)
