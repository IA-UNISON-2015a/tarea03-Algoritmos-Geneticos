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
#import time

__author__ = 'Erick Fernando López Fimbres'

class ProblemaNreinas(genetico.Problema):
    """
    Las N reinas para AG

    """
    def __init__(self, n=8):
        self.n = n

    def estado_aleatorio(self):
        estado = list(range(self.n))
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
    """
    32 reinas:
        
    64 reinas:
        tardo en promedio 4 minutos con los sig. valores:
            n_poblacion=300
            generaciones=400
            prob_mutacion=0.01
            
    32 reinas:
        tardo en promedio 22 seg con los sig. valores
        n_poblacion=100
        generaciones=400
        prob_mutacion=0.02
    
    8 reinas
        tardo en promedio .14 seg con los sig. valores
        n_poblacion=20
        generaciones=100
        prob_mutacion=0.02
    
    """
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun
    #       tu experiencia?
    """
    Hay que poner una poblacion mas o menos chica y tener un numero de
    generaciones muco mayor para asi ir afinando a los individuos mas
    optimos, aunque cabe resaltar que cuando los individuos no salen del minimo
    global entonces es cuando la mutacion hace el paro por eso tambien es
    importante variarla dependiendo de como se comporte la pobñación.
    
    """
    n_poblacion = 20
    generaciones =100
    prob_mutacion = 0.02
    
    
    alg_gen = genetico.GeneticoPermutaciones(ProblemaNreinas(8),
                                                 n_poblacion, prob_mutacion)
    
    solucion = prueba_genetico(alg_gen, generaciones, True)
    
    """
    alg_gen = genetico_tarea.GeneticoPermutacionesPropio(ProblemaNreinas(8),
                                                 n_poblacion, prob_mutacion)
    
    solucion = prueba_genetico(alg_gen, generaciones, True)
    """
    
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
    """
    8 reinas con
        n_poblacion = 50
        generaciones = 100
        prob_mutacion=0.02
        tiempo_promedio = 2.5 seg
        
    16 reinas con
        n_poblacion = 80
        generaciones = 300
        prob_mutacion=0.2
        tiempo_promedio = 15.8 seg
    """
    #
    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #
    """
    Depende mucho de el problema y tambien los metodos que implementaste
    para realizar tu algoritmo genetico, en veces te va aconvenir no tener mucha
    poblacion por la manera en que se realizan estos metodos.
    
    Entonces cuando necesitas 
    hacer variar  un poco la poblacion es recomendable poner una prob de mutacion
    un poco alta en uno de mis casos que tuve fue de que lo mejor que obtenia era costo 1
    pero al elevar la mutacion hizo que pudiera encontrar el optimo global
    Tambien aveces es recomendable tener poco numero de poblacion y mas o menos 
    varias generaciones doble o el triple de la población
    """