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
from random import randint
import genetico_nreinas

__author__ = 'Tu nombre'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'propuesto por Roberto Salazar'
        super().__init__(problema, n_población)
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        #

    def torneo(self):
        n1 = randint(0,self.n_población)
        n2 = randint(0,self.n_población)
        while n2 == n1:
            n2 = randint(0,self.n_población)
        a1,a2 = self.población[n1][0],self.población[n2][0]
        return n1 if a1 > a2 else n2

    @staticmethod
    def estado_a_cadena(estado):
        """
        Convierte un estado a una cadena de cromosomas

        @param estado: Una tupla con un estado
        @return: Una lista con una cadena de caracteres

        Por default converte el estado en una lista.

        """
        #se genera una lista con los numeros de 0 a n
        lista = list(range(len(estado)))
        #se inicializa la cadena como una lista vacía
        cadena = []
        for v in range(len(estado) - 1):
            #se busca la posición del elemento en la lista
            i = lista.index(estado[v])
            #se saca el elemento de la lista
            lista.pop(i)
            #se agrega el indice del elemento a la cadena
            cadena.append(i)
        print(estado,cadena)
        return cadena

    @staticmethod
    def cadena_a_estado(cadena):
        """
        Convierte una cadena de cromosomas a un estado

        @param cadena: Una lista de cromosomas o valores
        @return: Una tupla con un estado válido

        Por default convierte la lista a tupla

        """
        lista = list(range(len(cadena) + 1))
        estado = []
        for i in cadena:
            v = lista[i]
            lista.pop(i)
            estado.append(v)
        estado.append(lista[0])
        return estado

    def adaptación(self, individuo):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado
        mejor, mayor costo, menor adaptción.

        @param individuo: Una lista de cromosomas
        @return un número con la adaptación del individuo

        Por default usa 1 / (costo(estado) + 1)
        """
        return 1 / (1.0 + self.problema.costo(self.cadena_a_estado(individuo)))

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        raise NotImplementedError("¡Este metodo debe ser implementado!")

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        raise NotImplementedError("¡Este metodo debe ser implementado!")

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


if __name__ == "__main__":
    genetico = GeneticoPermutacionesPropio(genetico_nreinas.ProblemaNreinas(8), 10)
    print(genetico.población[0])
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    # g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    # genetico.prueba(g_propio)
