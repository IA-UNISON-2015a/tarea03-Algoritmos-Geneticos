#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
genetico_tarea.py
-----------------

En este módulo vas a desarrollar tu propio algoritmo
genético para resolver problemas de permutaciones

"""
import exp
import random
import genetico

__author__ = 'Erick Fernando López Fimbres'


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
        reescribir los métodos estáticos cadena_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'Erick Fernando Lopez Fimbres'
        
        #Ya inicializa la población
        super().__init__(problema, n_población)
        #porcentaje de cruza -->.6
        #seleccion: elitista o otro
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        #
        print(self.población)
        #self.p_muta=p_muta
        #self.p_cruza=p_cruza
        #self.tipo_selección=tipo_seleccion
        
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
        dominio=list(range(0,len(estado)))
        cadena=[]
        for x in range(len(estado)):
            cadena.append(dominio.index(estado[x]))
            dominio.remove(estado[x])
        
        return cadena
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
        #
        dominio=list(range(0,len(cadena)))
        estado=[]

        for x in range(len(cadena)):
            estado.append(dominio[cadena[x]])
            dominio.remove(dominio[cadena[x]])
    
        return tuple(estado)
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
        K=50
        return exp(-K*self.problema.costo(self.cadena_a_estado(individuo)))
        raise NotImplementedError("¡Este metodo debe ser implementado!")
    
    def torneoArtesMarciales(población):
        
        competidores=población[:]
        #varajeamos la poblacion
        random.shuffle(competidores)
        #escojemos 2 individuos 
        if(competidores[0][0] > competidores[1][0]):
            g1=competidores[0]
        else:
            g1=competidores[1]
        if(competidores[-1][0] > competidores[-2][0]):
            g2=competidores[-1]
        else:
            g2=competidores[-2]
        #regresamos los que tengan mejor adaptacion
        return (g1,g2)
    
    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        
        return [self.torneoArtesMarciales()
                for _ in range(self.n_población)]

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
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    genetico.prueba(g_propio)
