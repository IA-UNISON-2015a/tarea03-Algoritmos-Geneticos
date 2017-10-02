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
from itertools import combinations
from operator import itemgetter
from numpy import modf, exp

__author__ = 'Carlos Huguez'


class GeneticoPermutacionesPropio( genetico.Genetico ):
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
        self.nombre = 'Carlos Huguez'
        super().__init__( problema, n_población )
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
        #raise NotImplementedError("¡Este metodo debe ser implementado!")

        return [ i for i in estado ]

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
        
        return tuple( i for i in cadena )

    def adaptación(self, individuo):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado
        mejor, mayor costo, menor adaptción.

        @param individuo: Una lista de cromosomas
        @return un número con la adaptación del individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        
        return 1 / ( self.problema.costo( individuo ) )

    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        
        #Muestreo Deterministico
        
        sigma = sum( [  i[0] for i in self.población ] )
        ia = []
        valesp = ps = 0

        for ( indi, (apt, individuo) ) in enumerate( self.población ):

            ps = float( apt / sigma )
            
            valesp = ps * self.n_población

            fraccion, entera = modf( valesp )            
            
            ia.append( ( indi, entera, fraccion, individuo ) )

        ia.sort( key = lambda tup: tup[2], reverse = True )

        return [ ( ia[i][0] ,ia[i+1][0] ) for i in range(0,self.n_población, 2 ) ]

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

        individuo = []
        
        for i in range(0, int(len( cadena1 )/2) ):
            individuo.append( cadena1[i] )    

        for i in range( len( cadena2 ) ):
            if cadena2[i] not in individuo:
                individuo.append( cadena2[i] )    
        
        return individuo

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
        #Mutacion Heuristica

        pm = 1.0 / len( individuos[0] )
        lamda = random.randint( 2, len( individuos[0] ) )
                
        posicion_alearoria = []
        aux = 0
        while len( posicion_alearoria ) < lamda:
            aux = random.randint( 0, len( individuos[0] ) - 1 )    
            if aux not in posicion_alearoria:
                posicion_alearoria.append( aux )

        ia = []
        matriz_individuos_aux = []
        for individuo in individuos:   
            if random.random() <= pm:
                 
                for ( c1, c2 ) in combinations( posicion_alearoria, 2 ):
                    
                    ia = [ i for i in individuo ]
                    
                    individuo[c1], individuo[c2] =  individuo[c2], individuo[c1]
                    
                    matriz_individuos_aux.append( ( self.adaptación( ia ),  [ i for i in individuo ] ) )
                    
                    individuo = list( ia )

                matriz_individuos_aux.sort( key = lambda tup: tup[0] )
                individuo[:]
                individuo = [ i for i in matriz_individuos_aux[0][1] ]
                
                del matriz_individuos_aux[:]

    def reemplazo_generacional(self, individuos ):
        """
        Realiza el reemplazo generacional diferente al elitismo

        @param individuos: Una lista de cromosomas de hijos que pueden
                           usarse en el reemplazo
        @return: None (todo lo cambia internamente)

        Por default usamos solo el elitismo de conservar al mejor, solo si es
        mejor que lo que hemos encontrado hasta el momento.

        """
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #Torneo de padres
        wawa = []

        for i in range( 0, len( self.población ), 2 ):    
        
            if self.adaptación( self.población[i][1] ) > self.adaptación( self.población[i+1][1] ):
                wawa.append( ( self.población[i][0] , [ i for i in self.población[i][1] ] ) )
            else:
                wawa.append( ( self.población[i+1][0] , [ i for i in self.población[i+1][1] ] ) )
        
        for individuo in individuos:
            wawa.append( ( self.adaptación( individuo ), individuo ) )

        del self.población[:]

        self.población = list( wawa )

if __name__ == "__main__":
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio( genetico.ProblemaTonto(10), 10 )
    genetico.prueba( g_propio )
