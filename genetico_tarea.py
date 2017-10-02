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
from random import random
import genetico_nreinas
import heapq
from time import time

__author__ = 'José Roberto Salazar Espinoza'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población,prob_muta=0.01):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.prob_muta = prob_muta
        self.nombre = 'propuesto por Roberto Salazar'
        super().__init__(problema, n_población)

    def torneo(self,población):
        #se generan dos indices aleatorios diferentes
        n1 = randint(0,len(población) - 1)
        n2 = randint(0,len(población) - 1)
        while n2 == n1:
            n2 = randint(0,len(población) - 1)
        a1,a2 = población[n1][0],población[n2][0]
        #regresa el mas adaptado de los dos
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
        return cadena

    @staticmethod
    def cadena_a_estado(cadena):
        """
        Convierte una cadena de cromosomas a un estado

        @param cadena: Una lista de cromosomas o valores
        @return: Una tupla con un estado válido

        Por default convierte la lista a tupla

        """
        #se inicializa la lista de 0 a n
        lista = list(range(len(cadena) + 1))
        #el estado inicialmente es una lista vacía
        estado = []
        for i in cadena:
            #se saca el valor que corresponde al elemento i
            v = lista[i]
            #se elimina el elemento i de la lista
            lista.pop(i)
            #se agrega el valor del elemento i a el estado
            estado.append(v)
        #el último elemento que queda en la lista también se agrega a la lista
        estado.append(lista[0])
        return tuple(estado)

    def adaptación(self, individuo):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado
        mejor, mayor costo, menor adaptción.

        @param individuo: Una lista de cromosomas
        @return un número con la adaptación del individuo

        Por default usa 1 / (costo(estado) + 1)
        """
        #función de adaptación es el negativo del costo
        return -self.problema.costo(self.cadena_a_estado(individuo))

    def selección_individual(self):
        """
        Realiza una única pareja por medio de la ruleta

        @return: Una tupla con los pares a unirse

        """
        #hace practicamente lo mismo que la definida en genetico.py solo que
        #ahora es con torneos
        i = self.torneo(self.población)
        j = self.torneo(self.población[:i] + self.población[i+1:])
        return i, j if j < i else j+1

    def selección(self):
        """
        Selección por torneos.

        """
        return [self.selección_individual()
                for _ in range(self.n_población)]

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #cruza con 2 cortes sencilla
        n = len(cadena1)
        for i in range(n):
            corte1 = randint(0,n-2)
            corte2 = randint(0,n-2)
            while corte1 == corte2:
                corte2 = randint(0,n-2)
            mayor,menor = max((corte1,corte2)),min((corte1,corte2))
            hijo = cadena2[:menor] + cadena1[menor:mayor] + cadena2[mayor:]
        return hijo

    def mutación(self, individuos):
        """

        @param poblacion: Una lista de individuos (listas).

        @return: None, es efecto colateral mutando los individuos
                 en la misma lista

        """
        #muta todos los elementos de cada individuo con probabilidad prob_muta
        n = len(individuos[0])
        for individuo in individuos:
            for i in range(n):
                if random() < self.prob_muta:
                    individuo[i] = randint(0,n-i)


    def reemplazo_generacional(self, individuos):
        """
        Realiza el reemplazo generacional

        @param individuos: Una lista de cromosomas de hijos que pueden
                           usarse en el reemplazo
        @return: None (todo lo cambia internamente)

        Por default usamos solo el elitismo de conservar al mejor, solo si es
        mejor que lo que hemos encontrado hasta el momento.

        """
        #mete los 5 mejores individuos a la nueva población
        reemplazo = [(self.adaptación(individuo), individuo)
                     for individuo in individuos]
        nmejores = heapq.nlargest(5,self.población)
        reemplazo.extend(nmejores)
        reemplazo.sort(reverse=True)
        self.población = reemplazo[:self.n_población]

if __name__ == "__main__":
    genetico = GeneticoPermutacionesPropio(genetico_nreinas.ProblemaNreinas(16), 120,0.08)
    t_inicial = time()
    estado = genetico.busqueda(150)
    t_final = time()
    print(estado,genetico.problema.costo(estado))
    print("tiempo: ",t_final - t_inicial)
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    # g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    # genetico.prueba(g_propio)
