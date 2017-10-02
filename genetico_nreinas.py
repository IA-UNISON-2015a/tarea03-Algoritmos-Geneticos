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
from tabulate import tabulate

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
    """
    if verbose:
        print("\nUtilizando el AG: {}".format(algo_genetico.nombre))
        print("Con poblacion de dimensión {}".format(
            algo_genetico.n_población))
        print("Con {} generaciones".format(n_generaciones))
        print("Costo de la solución encontrada: {}".format(
            algo_genetico.problema.costo(solucion)))
        print("Tiempo de ejecución en segundos: {}".format(
            t_final - t_inicial))
    """
    return algo_genetico.problema.costo(solucion),t_final - t_inicial


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
    # reinas    poblacion    generaciones    proba           t    c
    #--------  -----------  --------------  -------  ----------  ---
    #       8          100              50     0.03   0.328175     0
    #      16          100              50     0.05   0.531327     0
    #      32          100             100     0.01   2.61825      0
    #      64          100             150     0.01  12.2009       7
    #
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun
    #       tu experiencia?
    
    #   Considerando la tabla que se generó variando todos los parámetros, se encontró
    #   una diferencia significativa a mayor cantidad de generaciones y menor probabilidad
    #    de mutación.
    #

    """
    n_poblacion = 64
    generaciones = 100
    prob_mutacion = 0.05
    
    
    fila=[]
    for r in [8,16,32,64]:
        for n_poblacion in [20,40,60,80,100]:
            for generaciones in [50,100,150]:
                for prob_mutacion in [0.01,0.03,0.05,0.1,0.3,0.5,0.8]:
                    alg_gen = genetico.GeneticoPermutaciones(ProblemaNreinas(r),
                                                         n_poblacion, prob_mutacion)
                    c,t= prueba_genetico(alg_gen, generaciones, True)
                    fila.append([r,n_poblacion,generaciones,prob_mutacion,t,c])
        
    
    print (tabulate(fila, headers=['reinas', 'poblacion','generaciones','proba','t','c']))
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
    # reinas    poblacion    generaciones    proba           t    c
    #--------  -----------  --------------  -------  ----------  ---
    #       8           20             100     0.5    0.125018     0
    #      16           40              50     0.8    0.312546     2
    #      32           80              50     0.01   2.33855      9
    #      64           40              50     0.1    4.73509     24
    #
    #
    # con elitísmo:
    #
    # reinas    poblacion    generaciones    proba           t    c
    #--------  -----------  --------------  -------  ----------  ---
    #       8           80             100     0.1    0.260159     0
    #      16           80             150     0.1    0.848499     0
    #      32           80             100     0.1    2.18129      5
    #      64           80             150     0.1   12.5823      15
    #      

    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #       En éste caso la probabilidad de mutación más conveniente fue de 0.1,
    #       con los valores más bajos se obtuvieron peores resultados.
    #       Con respecto a la población en términos generales entre más gande, mejores
    #      resultados aunque se tenían excepciones, lo mismo con las generaciones.
    #   
    #

    fila=[]
    for r in [8,16,32,64]:
        for n_poblacion in [20,40,60,80]:
            for generaciones in [50,100,150]:
                for prob_mutacion in [0.01,0.05,0.10,0.5,0.8]:
                    alg_gen = genetico_tarea.GeneticoPermutacionesPropio(ProblemaNreinas(r),
                                                         n_poblacion, prob_mutacion)
                    c,t= prueba_genetico(alg_gen, generaciones, True)
                    fila.append([r,n_poblacion,generaciones,prob_mutacion,t,c])
        
    
    print (tabulate(fila, headers=['reinas', 'poblacion','generaciones','proba','t','c']))