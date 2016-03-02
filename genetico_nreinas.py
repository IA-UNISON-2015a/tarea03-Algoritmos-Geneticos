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
    #
    #
    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #
    # 8 reinas = 32, 30 (Costo 0)
    # 16 reinas = 64,120  (Costo 0 en la mayoria de las veces, 1 a veces)
    # 32 reinas = 

    n_poblacion = 32
    generaciones = 30
    prob_mutacion = 0.05

    alg_gen = genetico.GeneticoPermutaciones1(nreinas.ProblemaNreinas(8),
                                              n_poblacion, prob_mutacion)

    solucion = prueba_genetico(alg_gen, n_poblacion, generaciones, True)
    print solucion

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
    # 8 reinas = 32,30 (costo 0 excepto en raras ocasiones)
    # 16 reinas = no pude encontrar nada que me diera costo 0 consistentemente (con 100,1000 me da costo 2)
    # 32 reinas = menos :(

    n_poblacion, generaciones = 400, 12
    #Agrega aqui las variables propias de tu algoritmo
    alg_gen = genetico.GeneticoPermutaciones2(nreinas.ProblemaNreinas(16),
                                                n_poblacion)
    solucion = prueba_genetico(alg_gen, n_poblacion, generaciones, True)
    print solucion
