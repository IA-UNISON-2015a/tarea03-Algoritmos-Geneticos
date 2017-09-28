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

__author__ = 'Tu nombre'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, población, prob_muta=.1):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'propuesto por el alumno'
        super().__init__(problema, población)
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        #
        self.prob_muta = prob_muta

    @staticmethod
    def estado_a_cadena(estado):
        """
        Convierte un estado a una cadena de cromosomas independiente
        del problema de permutación

        @param estado: Una tupla con un estado
        @return: Una lista con una cadena de caracteres

        """
        #
        # ------ I1MPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        return list(estado)
        raise NotImplementedError("¡Este metodo debe ser implementado!")

    @staticmethod
    def cadena_a_estado(cadena):
        """
        2Convierte una cadena de cromosomas a un estado donde el estado es
        una posible solución a un problema de permutaciones

        @param cadena: Una lista de cromosomas o valores
        @return: Una tupla con un estado válido

        """
        #
        # ------ I1MPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        return tuple(cadena)
        raise NotImplementedError("¡Este metodo debe ser implementado!")


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
        raise NotImplementedError("¡Este metodo debe ser implementado!")

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ I1MPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        # aqui estoy escribiendo codigo y esta bien chingon xddd
        parejas = []
        for i in range(0,len(self.población)-1):
            a = random.randint(0,len(self.población)-1)
            b = random.randint(0,len(self.población)-1)
            indiv1 = a if self.población[a][0] > self.población[b][0] else b
            a = random.randint(0,len(self.población)-1)
            b = random.randint(0,len(self.población)-1)
            indiv2 = a if self.población[a][0] > self.población[b][0] else b
            parejas.append((indiv1,indiv2))
        return parejas
        raise NotImplementedError("¡Este metodo debe ser implementado!")

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        # ------ I1MPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        print(cadena1)
        print(cadena2)
        a = random.randint(0,len(cadena1)-1)
        child = (cadena1[:a]+cadena2[a:])
        no_aparece = []
        for i in range(0,len(child)):
            if i not in child:
                no_aparece.append(i)
        return list(set(child)) + no_aparece
        raise NotImplementedError("¡Este metodo debe ser implementado!")

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
        # ------ I1MPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        for i in individuos:
            for j in range(len(i)):
                if random.random() < self.prob_muta:
                    k = random.randint(0,len(i)-1)
                    i[j],i[k] = i[k],i[j]
        return
        raise NotImplementedError("¡Este metodo debe ser implementado!")

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
