#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prueba de los algoritmos genéticos utilizando el problema
de las n-reinas para aprender a ajustarlos y probarlos.

"""

from time import time
from itertools import combinations
import random
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
        random.shuffle(estado)
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
    costo = algo_genetico.problema.costo(solucion)
    if verbose:
        print("\nUtilizando el AG: {}".format(algo_genetico.nombre))
        print("Con poblacion de dimensión {}".format(
            algo_genetico.n_población))
        print("Con {} generaciones".format(n_generaciones))
        print("Costo de la solución encontrada: {}".format(
            algo_genetico.problema.costo(solucion)))
        print("Tiempo de ejecución en segundos: {}".format(
            t_final - t_inicial))
    return costo, t_final-t_inicial


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
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun
    #       tu experiencia?
    #
    """
    b_tiempo = 100.0
    b_poblacion = 0.0
    b_gene = 0.0
    b_prob_mut = 0.0
    sol = 50
    
    tiempos = []
    poblacion = []
    gene = []
    prob_mut = []
    
    
    for i in range(50):
        
        n_poblacion = random.randint(1, 10) * 50
        generaciones = random.randint(1, 15) * 20
        prob_mutacion = random.random()
    
        alg_gen = genetico_tarea.GeneticoPermutacionesPropio(ProblemaNreinas(64),
                                                 n_poblacion, prob_mutacion)
        solucion, tiempo = prueba_genetico(alg_gen, generaciones, False)
        
        tiempos.append(tiempo)
        poblacion.append(n_poblacion)
        gene.append(generaciones)
        prob_mut.append(prob_mutacion)
        
        if solucion is 0  and tiempo < b_tiempo:
            b_tiempo = tiempo
            b_poblacion = n_poblacion
            b_gene = generaciones
            b_prob_mut = prob_mutacion
            sol = solucion
        
        if solucion is 0:
            print("Solucion encontrada:")
            print("Tiempo: {}".format(b_tiempo))
            print("poblacion {}".format(b_poblacion))
            print("Generaciones : {}".format(b_gene))
            print("Prob_mut: {}".format(b_prob_mut))
            print("Solucion: {}".format(sol))
            
    print("Tiempos: {}".format(tiempos))
    print("poblacion {}".format(poblacion))
    print("Generaciones : {}".format(gene))
    print("Prob_mut: {}".format(prob_mut))
    
    print("mejores: ****************************")
    print("Tiempo: {}".format(b_tiempo))
    print("poblacion {}".format(b_poblacion))
    print("Generaciones : {}".format(b_gene))
    print("Prob_mut: {}".format(b_prob_mut))
    print("Solucion: {}".format(sol))
    
    """
    n_poblacion = 250
    generaciones = 180
    prob_mutacion = 0.11
   
    """alg_gen = genetico.GeneticoPermutaciones(ProblemaNreinas(64),
                                             n_poblacion, prob_mutacion)
    solucion = prueba_genetico(alg_gen, generaciones, True)"""
    
    alg_gen2 = genetico_tarea.GeneticoPermutacionesPropio(ProblemaNreinas(64),
                                             n_poblacion, prob_mutacion)
    
    solucion2 = prueba_genetico(alg_gen2, generaciones, True)

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
    #
    #
    #   -- ¿Que reglas podrías establecer para asignar valores
    #       segun tu experiencia?
    #
