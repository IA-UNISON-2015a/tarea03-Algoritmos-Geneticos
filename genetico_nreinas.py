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
    #       
    #       para 8 reinas poblacion de 32 y generacion de 50  con prob_ de muta de .05 
    #       para 16 reinas poblacion de 64  generacion de 140 y prob_muta de .04 a .05
    #       para 32 reinas con una poblacion de 100 y con generaciones mayores a 350 
    #       y con prob_muta menores a .05
    #       para 64 reinas con poblacion de 120 y 700 generacions con prob_muta de .01
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun
    #       tu experiencia?
    #       en casi todos los casos los mejores parametros fueron las generaciones
    #       y para n grandes la prob_muta menor a .05
    #       
    #       
    #
   
    n_poblacion = 120
    generaciones = 700
    prob_mutacion = 0.01
    """
    alg_gen = genetico.GeneticoPermutaciones(ProblemaNreinas(64),
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
    #       para mis resultados no encontre muchas diferencias a los anteriores
    #       solo que si tuve que elevar la probabilidad de mutacion ya que 
    #       mi mutacion solo hace un cambio por individuo y doblar las generaciones
    #       obteniendo casi los mismos tiempos
    #
    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #       los parametros esta entre la probabilidad de mutacion alta y las generaciones
    #       
    #       no estoy orgulloso porque no funciona como esperaba 
    
    n_poblacion = 150
    generaciones = 1000
    prob_mutacion = 0.5
    
    alg_gen = genetico_tarea.GeneticoPermutacionesPropio(ProblemaNreinas(32),
                                             n_poblacion, prob_mutacion)

    solucion = prueba_genetico(alg_gen, generaciones, True)
