#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prueba de los algoritmos genéticos utilizando el problema
de las n-reinas para aprender a ajustarlos y probarlos.

"""

from time import time
from itertools import combinations
from random import shuffle
import genetico
import genetico_tarea

__author__ = 'juliowaissman'

class ProblemaNreinas(genetico.Problema):
    """
    Las N reinas para AG

    """
    def __init__(self, n=8):
        self.n = n

    def estado_aleatorio(self):
        estado = list( range( self.n ) )
        shuffle(estado)
        return tuple(estado)

    def costo(self, estado):
        """
        Calcula el costo de un estado por el número de conflictos entre reinas

        @param estado: Una tupla que describe un estado

        @return: Un valor numérico, mientras más pequeño, mejor es el estado.

        """
        return sum([1 for (i, j) in combinations(range(self.n), 2)
                    if abs(estado[i] - estado[j]) == abs(i - j)])


def prueba_genetico(algo_genetico, n_generaciones, verbose=False):
    """
    Prueba de los algoritmos genéticos con el problema de las n reinas
    desarrollado para búsquedas locales (tarea 2).

    @param algo_genetico: objeto de la clase genetico.Genetico
    @param n_generaciones: Generaciones (iteraciones) del algortimo
    @param verbose: True si quieres desplegar informacion básica
    @return: Un estado con la solucion (una permutacion de range(n)

    """
    t_inicial = time()
    solucion = algo_genetico.busqueda(n_generaciones)
    t_final = time()
    if verbose:
        print("\nUtilizando el AG: {}".format(algo_genetico.nombre))
        print("Con poblacion de dimensión {}".format(
            algo_genetico.n_población))
        print("Con {} generaciones".format(n_generaciones))
        print("Costo de la solución encontrada: {}".format(
            algo_genetico.problema.costo(solucion)))
        print("Tiempo de ejecución en segundos: {}".format(
            t_final - t_inicial))
    
    return solucion


if __name__ == "__main__":

    # Modifica los parámetro del algoritmo genetico que propuso el
    # profesor (el cual se conoce como genetico.GeneticoPermutaciones)
    # buscando que el algoritmo encuentre SIEMPRE una solución óptima,
    # utilizando el menor tiempo posible en promedio. Realiza esto
    # para las 8, 16, 32 y 64 reinas.
    #
    # Lo que puedes modificar es el tamaño de la población, el número
    # de generaciones y/o la probabilidad de mutación.
    #
    # Recuerda que podrias automatizar el problema haciendo una
    # función que genere una tabla con las soluciones, o hazlo a mano
    # si eso ayuda a comprender mejor el algoritmo.
    #
    #   -- ¿Cuales son en cada caso los mejores valores?  (escribelos
    #       abajo de esta linea)
    #       se realizaron combinaciones de:
    #       reinas = 8, 16, 32, 64
    #       poblacion = 10, 50, 100, 200         
    #       generaciones = 20, 100, 200, 400
    #       mutacion = 0.01, 0.05, 0.1
    #       
    #       las mejores soluciones fueron
    #       con 16 reinas, poblacion de 200 individuos, 100 generaciones        
    #       y probabilidad de mutacion de 0.1
    #            
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun
    #       tu experiencia?
    #       en mi experiencias seria tener una mayor cantidad de individos
    #       que de generaciones 
    #       
    #

    reinas = 16
    n_poblacion = 10
    generaciones = 100
    prob_mutacion = 0.1

    alg_gen = genetico_tarea.GeneticoPermutacionesPropio( ProblemaNreinas(reinas),
                                             n_poblacion)

    solucion = prueba_genetico(alg_gen, generaciones, True)

    # Modifica los parámetro del algoritmo genetico que propusite tu
    # mismo (el cual se conoce como
    # genetico_tarea.GeneticoPermutacionesPropio). De ser muchos
    # parámetros, restringete a 2 o 3, buscando que el algoritmo
    # encuentre SIEMPRE una solución óptima, utilizando el menor
    # tiempo posible en promedio. Realiza esto para las 8, 16, 32 y 64
    # reinas.
    #
    #   -- ¿Cuales son en cada caso los mejores valores?
    #       (escribelos abajo de esta linea)
    #       se realizo el mismo porcedimiento que arriba  
    #       estos fueron los mejores: 
    #       16 reinas con 10 individuos en la poblacion y 100 generaciones
    #       ( la mutacion la tengo establecida por 1/L )
    #   
    #   
    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #       en este caso seria tener menos individuos y muchas generaciones
    
