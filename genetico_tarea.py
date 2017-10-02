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
import math
import statistics as stats

__author__ = 'Tu nombre'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población, prob_muta=0.03,k=2):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadea_a_estado y
        estado_a_cadena).

        """
        self.prob_muta = prob_muta
        self.k=k
        self.nombre = 'propuesto por Belen'
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
        raise NotImplementedError("¡Este metodo debe ser implementado!")

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
        return tuple(cadena)
        #
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
        # habia intentado ésta pero daba resultados muy deprimentes
        # return math.exp(self.k*self.problema.costo(self.cadena_a_estado(individuo)))
        
        
        return 1 / (1.0 + self.k*self.problema.costo(self.cadena_a_estado(individuo)))
        
        raise NotImplementedError("¡Este metodo debe ser implementado!")

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        # Se revolverán todos los elementos de la población y se seleccionarán..
        # el primero con el último, el segundo con el penúltimo etc...
        #
         
        #aún no se si ordenar a la apoblación....
        población = self.población[:]
        población.sort()
        n = len(población)
        
        return [ (i,(i+1)%n)for i in range(n)]

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
        auxiliar = cadena1[:] if random.random() < 0.5 else cadena2[:]
        hijo=[]
        for i in range(len(cadena1)):
           
            if i%2==0:
                hijo.append(cadena1[i] if cadena1[i] not in hijo else cadena2[i] if cadena2[i] not in hijo else auxiliar.pop(0))
    
            else:
                hijo.append(cadena2[i] if cadena2[i] not in hijo else cadena1[i] if cadena1[i] not in hijo else auxiliar.pop(0))
            
            if hijo[i] in auxiliar:
                auxiliar.remove(hijo[i])

            
        return hijo
         
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
        
        dim = len(individuos[0])
        
        if random.random() < self.prob_muta:
            for individuo in individuos:
                aux=individuo[0]
                for i in range(1,dim):
                    individuo[i-1] = individuo[i]
                individuo[dim-1]=aux
            
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
        # La primera opción fue considerando la media de las adaptacinones, los
        # más cercanos a ella sobreviven
        """
        prom = stats.mean([self.adaptación(individuo) for individuo in individuos])
        reemplazo = [(abs(self.adaptación(individuo)-prom), individuo)
                     for individuo in individuos]
                     
        reemplazo.sort()
        
        self.población = [ (self.adaptación(reemplazo[i][1]), reemplazo[i][1]) for i in range(self.n_población)]
        """
        
         #La segunda opción fue aleatoria escoger "aleatoriamente"
        """
        reemplazo = [(self.adaptación(individuo), individuo)
                     for individuo in individuos]
                     
        random.shuffle(reemplazo)
        self.población = reemplazo[:self.n_población]
        """
        
        # la tercera fue nuevamente el elitísmo
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