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
import numpy as np

__author__ = 'Alexis Martinez'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población,prob_mut=.01):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'propuesto por el alumno Alexis Martinez'
        super().__init__(problema, n_población)
        #
        self.prob_mut = prob_mut
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
        return list(estado)
        #

    @staticmethod
    def cadena_a_estado(cadena):
        """
        Convierte una cadena de cromosomas a un estado donde el estado es
        una posible solución a un problema de permutaciones

        @param cadena: Una lista de cromosomas o valores
        @return: Una tupla con un estado válido

        """
        #
        return tuple(cadena)
        #

        
    def adaptación(self, individuo):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado
        mejor, mayor costo, menor adaptción.

        @param individuo: Una lista de cromosomas
        @return un número con la adaptación del individuo

        """
        #
        return 1/ (1.0 + self.problema.costo(self.cadena_a_estado(individuo)))
        #

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        parejas = []
        for _ in range(len(self.población)):
            
            c = np.random.randint(0,len(self.población),4)
            i = c[0] if self.población[c[0]][0] > self.población[c[1]][0] else c[1]
            j = c[2] if self.población[c[2]][0] > self.población[c[3]][0] else c[3]
            parejas.append((i,j))
            
        return parejas
        #

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        hijo = cadena1[:]
        len_cadena = len(hijo)
        corte1 = np.random.randint(0, len_cadena - 1)
        corte2 = np.random.randint(corte1 + 1, len_cadena)
        seg = hijo[corte1:corte2]
        aux = [i for i in cadena2 if i not in seg ]
        j=0
        for i in range(len_cadena):
            if hijo[i] not in seg:
                hijo[i] = aux[j]
                j += 1
                
        return hijo
        #

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
        # Utilice una mutacion por insercion 
        
        for individuo in individuos:
            if np.random.random() < self.prob_mut:
                k = np.random.randint(0, len(individuo),2)
                x = individuo.pop(k[0])
                individuo.insert(k[1],x)
                    
        #

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
        # No se me ocurrio mejor manera de hacer un remplazo generacional
        #
        reemplazo = [(self.adaptación(individuo), individuo)
                        for individuo in individuos]
        reemplazo.append(max(self.población))
        reemplazo.sort(reverse=True)
        self.población = reemplazo[:self.n_población]
        
        #



if __name__ == "__main__":
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    genetico.prueba(g_propio)
