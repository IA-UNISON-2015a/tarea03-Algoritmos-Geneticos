#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
genetico.py
------------

Este modulo incluye el algoritmo genérico para algoritmos genéticos, así como un
algoritmo genético adaptado a problemas de permutaciones, como el problema de las
n-reinas o el agente viajero.

Como tarea se pide desarrollar otro algoritmo genético con el fin de probar otro tipo
de métodos internos, así como ajustar ambos algortmos para que funcionen de la mejor
manera posible.


Para que funcione, este modulo debe de encontrarse en la misma carpeta que blocales.py
y nreinas.py vistas en clase.

"""

__author__ = 'Julio Waissman, Gerardo Tarragona'

import nreinas
import random
import time


class Genetico:

    """
    Clase genérica para un algoritmo genético.
    Contiene el algoritmo genético general y las clases abstractas.

    """

    def busqueda(self, problema, n_poblacion=10, n_generaciones=30, elitismo=True):
        """
        Algoritmo genético general

        @param problema: Un objeto de la clase blocal.problema
        @param n_poblacion: Entero con el tamaño de la población
        @param n_generaciones: Número de generaciones a simular
        @param elitismo: Booleano, para aplicar o no el elitismo

        @return: Un estado del problema

        """
        poblacion = [problema.estado_aleatorio() for _ in range(n_poblacion)]

        for _ in range(n_generaciones):

            aptitud = [
                self.calcula_aptitud(individuo, problema.costo) for individuo in poblacion]

            elite = min(poblacion, key=problema.costo) if elitismo else None

            padres, madres = self.seleccion(poblacion, aptitud)

            poblacion = self.mutacion(self.cruza_listas(padres, madres))

            poblacion = poblacion[:n_poblacion]

            if elitismo:
                poblacion.append(elite)

        e = min(poblacion, key=problema.costo)
        return e

    def calcula_aptitud(self, individuo, costo=None):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado mejor, por default
        es inversamente proporcionl al costo (mayor costo, menor adaptción).

        @param individuo: Un estado el problema
        @param costo: Una función de costo (recibe un estado y devuelve un número)

        @return un número con la adaptación del individuo
        """
        # return max(0, len(individuo) - costo(individuo))
        return 1.0 / (1.0 + costo(individuo))

    def seleccion(self, poblacion, aptitud):
        """
        Seleccion de estados

        @param poblacion: Una lista de individuos

        @return: Dos listas, una con los padres y otra con las madres.
        estas listas tienen una dimensión int(len(poblacion)/2)

        """
        raise NotImplementedError(
            "¡Este metodo debe ser implementado por la subclase!")

    def cruza_listas(self, padres, madres):
        """
        Cruza una lista de padres con una lista de madres, cada pareja da dos hijos

        @param padres: Una lista de individuos
        @param madres: Una lista de individuos

        @return: Una lista de individuos

        """
        hijos = []
        for (padre, madre) in zip(padres, madres):
            hijos.extend(self.cruza(padre, madre))
        return hijos

    def cruza(self, padre, madre):
        """
        Cruza a un padre con una madre y devuelve una lista de hijos, mínimo 2
        """
        raise NotImplementedError(
            "¡Este metodo debe ser implementado por la subclase!")

    def mutacion(self, poblacion):
        """
        Mutación de una población. Devuelve una población mutada

        """
        raise NotImplementedError(
            "¡Este metodo debe ser implementado por la subclase!")


class GeneticoPermutaciones1(Genetico):

    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """

    def __init__(self, prob_muta=0.01):
        """
        @param prob_muta : Probabilidad de mutación de un cromosoma (0.01 por defualt)

        """
        self.prob_muta = prob_muta
        self.nombre = 'propuesto por el profesor con prob. de mutación ' + \
            str(prob_muta)

    def seleccion(self, poblacion, aptitud):
        """
        Selección por torneo.


        """
        padres = []
        baraja = range(len(poblacion))
        random.shuffle(baraja)
        for (ind1, ind2) in [(baraja[i], baraja[i + 1]) for i in range(0, len(poblacion) - 1, 2)]:
            ganador = ind1 if aptitud[ind1] > aptitud[ind2] else ind2
            padres.append(poblacion[ganador])

        madres = []
        random.shuffle(baraja)
        for (ind1, ind2) in [(baraja[i], baraja[i + 1]) for i in range(0, len(poblacion) - 1, 2)]:
            ganador = ind1 if aptitud[ind1] > aptitud[ind2] else ind2
            madres.append(poblacion[ganador])

        return padres, madres

    def cruza(self, padre, madre):
        """
        Cruza especial para problemas de permutaciones

        @param padre: Una tupla con un individuo
        @param madre: Una tupla con otro individuo

        @return: Dos individuos resultado de cruzar padre y madre con permutaciones

        """
        hijo1, hijo2 = list(padre), list(madre)
        corte1 = random.randint(0, len(padre) - 1)
        corte2 = random.randint(corte1 + 1, len(padre))
        for i in range(len(padre)):
            if i < corte1 or i >= corte2:
                hijo1[i], hijo2[i] = hijo2[i], hijo1[i]
                while hijo1[i] in padre[corte1:corte2]:
                    hijo1[i] = madre[padre.index(hijo1[i])]
                while hijo2[i] in madre[corte1:corte2]:
                    hijo2[i] = padre[madre.index(hijo2[i])]
        return [tuple(hijo1), tuple(hijo2)]

    def mutacion(self, poblacion):
        """
        Mutación para individus con permutaciones. Utiliza la variable local self.prob_muta

        @param poblacion: Una lista de individuos (tuplas).

        @return: Los individuos mutados

        """
        poblacion_mutada = []
        for individuo in poblacion:
            individuo = list(individuo)
            for i in range(len(individuo)):
                if random.random() < self.prob_muta:
                    k = random.randint(0, len(individuo) - 1)
                    individuo[i], individuo[k] = individuo[k], individuo[i]
            poblacion_mutada.append(tuple(individuo))
        return poblacion_mutada


##########################################################################
#  AQUI EMPIEZA LO QUE HAY QUE HACER CON LA TAREA
##########################################################################

class GeneticoPermutaciones2(Genetico):

    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """

    def __init__(self):
        """
        Aqui puedes poner algunos de los parámetros que quieras utilizar en tu clase

        """
        self.nombre = 'Algoritmo Gerardijkstra'
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ------------------------------------
        #

    def calcula_aptitud(self, individuo, costo=None):
        """
        Desarrolla un método específico de medición de aptitud.

        """
        ####################################################################
        #                          20 PUNTOS
        ####################################################################
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        return max(0, len(individuo) - costo(individuo))

    def seleccion(self, poblacion, aptitud):
        """
        Desarrolla un método específico de selección.

        """
        #####################################################################
        #                          20 PUNTOS
        #####################################################################
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #

        acc = sum(aptitud)
        dardo = random.random()
        base = 0
        padres = []
        for (i, a) in enumerate(aptitud):
            base += a / acc
            if dardo <= base:
                padres.append(poblacion[i])

        base = 0
        dardo = random.random()
        madres = []
        for (i, a) in enumerate(aptitud):
            base += a / acc
            if dardo <= base:
                madres.append(poblacion[i])

        return padres, madres

    def cruza(self, padre, madre):
        """
        Cruza especial para problemas de permutaciones

        @param padre: Una tupla con un individuo
        @param madre: Una tupla con otro individuo

        @return: Dos individuos resultado de cruzar padre y madre con permutaciones

        """
        hijo1, hijo2 = list(padre), list(madre)
        corte1 = random.randint(0, len(padre) - 1)
        corte2 = random.randint(corte1 + 1, len(padre))
        for i in range(len(padre)):
            if i < corte1 or i >= corte2:
                hijo1[i], hijo2[i] = hijo2[i], hijo1[i]
                while hijo1[i] in padre[corte1:corte2]:
                    hijo1[i] = madre[padre.index(hijo1[i])]
                while hijo2[i] in madre[corte1:corte2]:
                    hijo2[i] = padre[madre.index(hijo2[i])]
        return [tuple(hijo1), tuple(hijo2)]

    def mutacion(self, poblacion):
        """
        Desarrolla un método específico de mutación.

        """
        ###################################################################
        #                          20 PUNTOS
        ###################################################################
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        poblacion_mutada = []
        for individuo in poblacion:
            individuo = list(individuo)
            individuo[0], individuo[
                len(individuo) - 1] = individuo[len(individuo) - 1], individuo[0]
            # for i in range(len(individuo)):
            #        individuo[i], individuo[len(individuo) - 1] = individuo[len(individuo) - 1], individuo[i]
            poblacion_mutada.append(tuple(individuo))
        return poblacion_mutada


def prueba_genetico_nreinas(algo_genetico, problema, n_poblacion, n_generaciones):
    tiempo_inicial = time.time()
    suma_tiempos = 0
    suma_costos = 0
    iter = 50
    for i in xrange(iter):
        solucion = algo_genetico.busqueda(
            problema, n_poblacion, n_generaciones, elitismo=True)
        tiempo_final = time.time()
        suma_tiempos += tiempo_final - tiempo_inicial
        suma_costos += problema.costo(solucion)

    print "\nUtilizando el algoritmo genético " + algo_genetico.nombre
    print "Con poblacion de dimensión ", n_poblacion
    print "Con ", str(n_generaciones), " generaciones"
    #print "Costo de la solución encontrada: ", problema.costo(solucion)
    #print "Tiempo de ejecución en segundos: ", tiempo_final - tiempo_inicial
    print iter, " iteraciones"
    print "Tiempo promedio >> ", suma_tiempos/100
    print "Costos promedio >> ", suma_costos/100
    return solucion


if __name__ == "__main__":

    ##########################################################################
    #                          20 PUNTOS
    ##########################################################################
    # Modifica los valores de la función siguiente (o el parámetro del algo_genetico)
    # buscando que el algoritmo encuentre SIEMPRE una solución óptima, utilizando el menor tiempo
    # posible en promedio. Realiza esto para las 8, 16 y 32 reinas.
    #   -- ¿Cuales son en cada caso los mejores valores (escribelos abajo de esta lines)
    #
    # Para las 8-reinas.
    # Con 50 iteraciones del algoritmo, encontre un tiempo promedio de .012 segundos
    # y un costo de 0

    # Para las 16-reinas
    # Con 50 iteraciones, encontre un tiempo de .25 segundos y un costo de 1
    
    # Para las 32-reinas
    # Con 50 iteraciones, se encontro un tiempo de 4 segundos y un costo de 4
    # Mientras mas se aumenta la poblacion o las generaciones es mas probable
    # disminuir el costo promedio, pero debido a la complejidad del problema
    # es necesario hacer un aumento bastante sustancial, y esto toma mucho
    # tiempo de ejecucion.

    # Para los tres casos de problema (8, 16 y 32 reinas) el cambio de probabi-
    # lidad en las mutaciones no influyo en la solucion del problema, los costos
    # no parecian variar.

    solucion = prueba_genetico_nreinas(algo_genetico=GeneticoPermutaciones1(.5),
                                       problema=nreinas.ProblemaNreinas(32),
                                       n_poblacion=50,
                                       n_generaciones=10)

    print solucion

    ##########################################################################
    #                          20 PUNTOS
    ##########################################################################
    # Modifica los valores de la función siguiente (o los posibles parámetro del algo_genetico)
    # buscando que el algoritmo encuentre SIEMPRE una solución óptima, utilizando el menor tiempo
    # posible en promedio. Realiza esto para las 8, 16 y 32 reinas.
    #   -- ¿Cuales son en cada caso los mejores valores (escribelos abajo de esta lines)
    #
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun tu experiencia? Escribelo aqui
    #   abajo, utilizando tnto espacio como consideres necesario.
    #
    # Recuerda de quitar los comentarios de las lineas siguientes:

    # solucion = prueba_genetico_nreinas(algo_genetico=GeneticoPermutaciones2(),
    #                                        problema=nreinas.ProblemaNreinas(32),
    #                                        n_poblacion=60,
    #                                        n_generaciones=10)
    # print solucion

    #   Para las 8-reinas.
    #   Con muchas pruebas, encontre que el promedio de tiempo es de entre
    #   .011.. y .012.. segundos y el costo de 0, estos datos, por cada 50
    #   iteraciones del algoritmo.
    #   Poblacion 20, 1 generacion

    #   Para las 16-reinas.
    #   El promedio de tiempo es de .29 segundos para cada 50 iteraciones
    #   del algoritmo con un costo de 1.
    #   Poblacion 100 y generaciones 30
    
    #   Para las 32-reinas.
    #   El promedio de tiempo es de .5 segundos por cada 50 iteraciones y un
    #   costo de 5.
    #   Poblacion 60, generaciones 10

    #   -- ¿Que reglas podrías establecer para asignar valores segun tu experiencia
    #   No es necesario asignar poblaciones y generaciones grandes al algoritmo
    #   si se quiere encontrar una solucion en un tiempo bastante razonable, sin
    #   importar el costo; en cambio si se quiere una solucion con un costo
    #   muy pequeno o 0, si se tendra que asignar una poblacion grande, pero el
    #   tiempo de ejecucion tomara mas tiempo
