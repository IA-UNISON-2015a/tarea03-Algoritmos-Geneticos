#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prueba de los algoritmos genéticos utilizando el problema
de las n-reinas para aprender a ajustarlos y probarlos.

"""

import time
import nreinas
import genetico

__author__ = 'juliowaissman'


def prueba_genetico(algo_genetico, n_poblacion, n_generaciones, verbose=False):
    """
    Prueba de los algoritmos genéticos con el problema delas n reinas
    desarrollado para búsquedas locales (tarea 2).

    @param algo_genetico: objeto de la clase genetico.Genetico
    @param n_poblacion: Población del algoritmo genético
    @param n_generaciones: Generaciones (iteraciones) del algortimo
    @param verbose: True si quieres desplegar informacion básica
    @return: Un estado con la solucion (una permutacion de range(n)

    """
    t_inicial = time.time()
    algo_genetico.inicializa_poblacion(n_poblacion)
    solucion = algo_genetico.busqueda(n_generaciones)
    t_final = time.time()
    if verbose:
        print "\nUtilizando el algoritmo genético " + algo_genetico.nombre
        print "Con poblacion de dimensión ", n_poblacion
        print "Con ", str(n_generaciones), " generaciones"
        print "Costo de la solución encontrada: ",
        print algo_genetico.problema.costo(solucion)
        print "Tiempo de ejecución en segundos: ", t_final - t_inicial
    return solucion


if __name__ == "__main__":

    ###########################################################################
    #                          20 PUNTOS
    ###########################################################################
    # Modifica los parámetro del algoritmo genetico que propuso el profesor
    # (el cual se conoce como genetico.GeneticoPermutaciones1), que en este
    # caso son población, generaciones y la probabilidad de mutación buscando
    # que el algoritmo encuentre SIEMPRE una solución óptima, utilizando el
    # menor tiempo posible en promedio. Realiza esto para las 8, 16, 32 y 64
    # reinas.
    #
    # Recuerda que podrias automatizar el problema haciendo una función que
    # genere una tabla con las soluciones, o hazlo a mano si eso ayuda a
    # comprender mejor el algoritmo.
    #
    #   -- ¿Cuales son en cada caso los mejores valores?
    #       (escribelos abajo de esta linea)
    #       8 reinas: 8,500,0.02
    #       16 reinas: 17,300,0.03
    #       32 reinas: 20,300,0.03
    #
    #
    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #       Se rige por el tamaño de la población, es el valor que determina cuantas generaciones se ocupan, como
    #       pude notar en 16 y 32 reinas, valores similares y tiempos cercanos (16 -> menos del segundo, 32 -> ~1.2 segundos)
    #

    # n_poblacion = 20
    # generaciones = 300
    #prob_mutacion = 0.03

    #alg_gen = genetico.GeneticoPermutaciones1(nreinas.ProblemaNreinas(32),
    #                                          n_poblacion, prob_mutacion)

    #solucion = prueba_genetico(alg_gen, n_poblacion, generaciones, True)
    #print solucion

    ###########################################################################
    #                          30 PUNTOS
    ###########################################################################
    # Modifica los parámetro del algoritmo genetico que propusite tu mismo
    # (el cual se conoce como genetico.GeneticoPermutaciones2), que en este
    # caso son población, generaciones y los parámetros que hayas agregado,
    # los cuales pueden ser muchos o pocos. De ser muchos restringete a 1 o 2,
    # buscando que el algoritmo encuentre SIEMPRE una solución óptima,
    # utilizando el menor tiempo posible en promedio. Realiza esto para las 8,
    # 16, 32 y 64 reinas.
    #
    #   -- ¿Cuales son en cada caso los mejores valores?
    #       (escribelos abajo de esta linea)
    #
    #
    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #

    n_poblacion = 200
    generaciones = 10
    prob_mutacion = 0.1
    # Agrega aqui las variables propias de tu algoritmo
    alg_gen = genetico.GeneticoPermutaciones2(nreinas.ProblemaNreinas(8), n_poblacion,prob_mutacion)
    solucion = prueba_genetico(alg_gen, n_poblacion, generaciones, True)
    print solucion
