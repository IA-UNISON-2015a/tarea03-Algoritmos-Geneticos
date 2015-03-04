#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

genetico.py
------------

Este modulo incluye el algoritmo genérico para algoritmos genéticos, así como un
algoritmo genético adaptado a problemas de permutaciones, como el problema de las
n-reinas o el agente viajero.

Como tarea se pide desarrollar otro algoritmo genético con el fin de probar otro tipo
de métodos internos, así como ajustar ambos algoritmos para que funcionen de la mejor
manera posible.

Para que funcione, este modulo debe de encontrarse en la misma carpeta que blocales.py
y nreinas.py vistas en clase.

"""

__author__ = 'Cruz Luque Juan Manuel'

import nreinas
import random
import time
from itertools import combinations


"""

Clase genérica para un algoritmo genético.
Contiene el algoritmo genético general y las clases abstractas.

"""

class Genetico:

    """

    Algoritmo genético general.

    @param problema: Un objeto de la clase blocal.problema
    @param n_poblacion: Entero con el tamaño de la población
    @param n_generaciones: Número de generaciones a simular
    @param elitismo: Booleano, para aplicar o no el elitismo

    @return: Un estado del problema

    """

    def busqueda(self, problema, n_poblacion=10, n_generaciones=30, elitismo=True):

        poblacion = [problema.estado_aleatorio() for _ in range(n_poblacion)]

        for _ in range(n_generaciones):

            aptitud = [self.calcula_aptitud(individuo, problema.costo) for individuo in poblacion]

            elite = min(poblacion, key = problema.costo) if elitismo else None

            padres, madres = self.seleccion(poblacion, aptitud)

            poblacion = self.mutacion(self.cruza_listas(padres, madres))

            poblacion = poblacion[:n_poblacion]

            if elitismo:
                poblacion.append(elite)

        e = min(poblacion, key = problema.costo)

        return e

    """

    Calcula la adaptación de un individuo al medio, mientras más adaptado mejor, por default
    es inversamente proporcionl al costo (mayor costo, menor adaptción).

    @param individuo: Un estado el problema
    @param costo: Una función de costo (recibe un estado y devuelve un número)

    @return un número con la adaptación del individuo

    """

    def calcula_aptitud(self, individuo, costo=None):

        """"

        return max(0, len(individuo) - costo(individuo))

        return 1.0 / (1.0 + costo(individuo))

        """

    """

    Seleccion de estados.

    @param poblacion: Una lista de individuos

    @return: Dos listas, una con los padres y otra con las madres.
    estas listas tienen una dimensión int(len(poblacion)/2)

    """

    def seleccion(self, poblacion, aptitud):

        raise NotImplementedError("¡Este metodo debe ser implementado por la subclase!")

    """

    Cruza una lista de padres con una lista de madres, cada pareja da dos hijos.

    @param padres: Una lista de individuos
    @param madres: Una lista de individuos

    @return: Una lista de individuos

    """

    def cruza_listas(self, padres, madres):

        hijos = []

        for (padre, madre) in zip(padres, madres):

            hijos.extend(self.cruza(padre, madre))

        return hijos

    """

    Cruza a un padre con una madre y devuelve una lista de hijos, mínimo 2.

    @param padre: Una lista de individuos
    @param madre: Una lista de individuos

    @return: Una lista de hijos

    """

    def cruza(self, padre, madre):

        raise NotImplementedError("¡Este metodo debe ser implementado por la subclase!")

    """

    Mutación de una población. Devuelve una población mutada.

    @param poblacion: Una lista de individuos

    @return: Una lista de individuos mutados

    """

    def mutacion(self, poblacion):

        raise NotImplementedError("¡Este metodo debe ser implementado por la subclase!")


"""

Clase con un algoritmo genético adaptado a problemas de permutaciones.

"""

class GeneticoPermutaciones1(Genetico):

    """

    @param prob_muta : Probabilidad de mutación de un cromosoma (0.01 por defualt)

    """

    def __init__(self, prob_muta = 0.01):

        self.prob_muta = prob_muta

        self.nombre = 'propuesto por el profesor con prob. de mutación ' + str(prob_muta)

    """

    Selección por torneo.

    @param poblacion: Una lista de individuos
    @param aptitud: Una lista con las aptitudes de los individuos

    @return: Dos listas, una con los padres y otra con las madres.
    estas listas tienen una dimensión int(len(poblacion)/2)

    """

    def seleccion(self, poblacion, aptitud):

        padres = []

        baraja = range(len(poblacion))

        random.shuffle(baraja)

        for (ind1, ind2) in [(baraja[i], baraja[i+1]) for i in range(0, len(poblacion)-1, 2)]:

            ganador = ind1 if aptitud[ind1] > aptitud[ind2] else ind2

            padres.append(poblacion[ganador])

        madres = []

        random.shuffle(baraja)

        for (ind1, ind2) in [(baraja[i], baraja[i+1]) for i in range(0, len(poblacion)-1, 2)]:

            ganador = ind1 if aptitud[ind1] > aptitud[ind2] else ind2

            madres.append(poblacion[ganador])

        return padres, madres

    """

    Cruza a un padre con una madre y devuelve una lista de hijos, mínimo 2.

    @param padre: Una lista de individuos
    @param madre: Una lista de individuos

    @return: Una lista de hijos

    """

    def cruza(self, padre, madre):

        hijo1, hijo2 = list(padre), list(madre)

        corte1 = random.randint(0, len(padre)-1)

        corte2 = random.randint(corte1+1, len(padre))

        for i in range(len(padre)):

            if i < corte1 or i >= corte2:

                hijo1[i], hijo2[i] = hijo2[i], hijo1[i]

                while hijo1[i] in padre[corte1:corte2]:

                    hijo1[i] = madre[padre.index(hijo1[i])]

                while hijo2[i] in madre[corte1:corte2]:

                    hijo2[i] = padre[madre.index(hijo2[i])]

        return [tuple(hijo1), tuple(hijo2)]

    """

    Mutación para individus con permutaciones. Utiliza la variable local self.prob_muta.

    @param poblacion: Una lista de individuos (tuplas)

    @return: Los individuos mutados

    """

    def mutacion(self, poblacion):

        poblacion_mutada = []

        for individuo in poblacion:

            individuo = list(individuo)

            for i in range(len(individuo)):

                if random.random() < self.prob_muta:

                    k = random.randint(0, len(individuo) - 1)

                    individuo[i], individuo[k] = individuo[k], individuo[i]

            poblacion_mutada.append(tuple(individuo))

        return poblacion_mutada


################################################################################################
#  AQUI EMPIEZA LO QUE HAY QUE HACER CON LA TAREA
################################################################################################

"""

Clase con un algoritmo genético adaptado a problemas de permutaciones.

"""

class GeneticoPermutaciones2(Genetico):

    """

    Aqui puedes poner algunos de los parámetros que quieras utilizar en tu clase.

    """

    def __init__(self, prob_muta = 0.01):

        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ------------------------------------------------------------------------
        #

        self.prob_muta = prob_muta

        self.nombre = 'propuesto por el alumno con prob. de mutación ' + str(prob_muta)

    """

    Desarrolla un método específico de medición de aptitud.

    """

    ####################################################################
    #                          20 PUNTOS
    ####################################################################
    #
    # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
    #

    def calcula_aptitud(self, individuo, costo=None):

        #return 1.0 / (1.0 + costo(individuo))
        return costo(individuo)

    """

    Desarrolla un método específico de selección.

    """

    #####################################################################
    #                          20 PUNTOS
    #####################################################################
    #
    # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
    #

    """

    Selección por ruleta.

    @param poblacion: Una lista de individuos
    @param aptitud: Una lista con las aptitudes de los individuos

    @return: Dos listas, una con los padres y otra con las madres.
    estas listas tienen una dimensión int(len(poblacion)/2)

    """

    def seleccion(self, poblacion, aptitud):

        # Suma de las aptitudes
        sa = sum(aptitud)

        # Media de la aptitud
        mf = float(sa)/len(aptitud)

        # Se calcula el valor esperado de cada individuo
        vei = []

        for i in aptitud:
            vei.append(float(i)/mf)

        # Suma de los valores esperados
        sve = sum(vei)

        # Tupla con el individuo,aptitud y valor esperado
        ind = zip(poblacion,aptitud,vei)

        #print ind

        padres = []

        suma = 0

        r = random.uniform(0, sve)

        x = 0

        #print 'numero aleatorio = ' + str(r)

        while x < len(aptitud) / 2:

            for i in ind:

                temp = i[2]

                suma += temp

                #print 'suma = ' + str(suma)

                if suma > r  and len(padres) < len(aptitud)/2:

                    #print 'hola'

                    padres.append(i[0])

                    suma = 0

                    r = random.uniform(0, sve)

                    x += 1

                    #print 'numero aleatorio = ' + str(r)

        #print 'PADRES'

        #print padres

        madres = []

        suma = 0

        r = random.uniform(0, sve)

        x = 0

        #print 'numero aleatorio = ' + str(r)

        while x < len(aptitud)/2:

            for i in ind:

                temp = i[2]

                suma += temp

                #print 'suma = ' + str(suma)

                if suma > r  and len(madres) < len(aptitud)/2:

                    #print 'hola'

                    madres.append(i[0])

                    suma = 0

                    r = random.uniform(0, sve)

                    x += 1

                    #print 'numero aleatorio = ' + str(r)

        #print 'MADRES'

        #print madres

        return padres, madres

    """

    Cruza a un padre con una madre y devuelve una lista de hijos, mínimo 2.

    @param padre: Una lista de individuos
    @param madre: Una lista de individuos

    @return: Una lista de hijos

    """

    def cruza(self, padre, madre):

        hijo1, hijo2 = list(padre), list(madre)

        corte1 = random.randint(0, len(padre)-1)

        corte2 = random.randint(corte1+1, len(padre))

        for i in range(len(padre)):

            if i < corte1 or i >= corte2:

                hijo1[i], hijo2[i] = hijo2[i], hijo1[i]

                while hijo1[i] in padre[corte1:corte2]:

                    hijo1[i] = madre[padre.index(hijo1[i])]

                while hijo2[i] in madre[corte1:corte2]:

                    hijo2[i] = padre[madre.index(hijo2[i])]

        return [tuple(hijo1), tuple(hijo2)]

    """

    Desarrolla un método específico de mutación.

    """

    ###################################################################
    #                          20 PUNTOS
    ###################################################################
    #
    # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
    #

    """

    Mutación para individus con permutaciones. Utiliza la variable local self.prob_muta. El metodo
    a utilizar es el metodo switch el cual intercambia dos valores a la siguiente posicion.
    ejemplo:
    1 2 3
    1 3 2

    @param poblacion: Una lista de individuos (tuplas)

    @return: Los individuos mutados

    """

    def mutacion(self, poblacion):

        poblacion_mutada = []

        for individuo in poblacion:

            individuo = list(individuo)

            for i in range(len(individuo)):

                if random.random() < self.prob_muta:

                    k = random.randint(0, len(individuo) - 1)

                    #print individuo

                    if (k == len(individuo) - 1):

                        individuo[k], individuo[0] = individuo[0], individuo[k]

                    else:

                        individuo[k], individuo[k+1] = individuo[k+1], individuo[k]

                    #print individuo

            poblacion_mutada.append(tuple(individuo))

        return poblacion_mutada

def prueba_genetico_nreinas(algo_genetico, problema, n_poblacion, n_generaciones):

    tiempo_inicial = time.time()

    solucion = algo_genetico.busqueda(problema, n_poblacion, n_generaciones, elitismo = True)

    tiempo_final = time.time()

    print "\nUtilizando el algoritmo genético " + algo_genetico.nombre

    print "Con poblacion de dimensión ", n_poblacion

    print "Con ", str(n_generaciones), " generaciones"

    print "Costo de la solución encontrada: ", problema.costo(solucion)

    print "Tiempo de ejecución en segundos: ", tiempo_final - tiempo_inicial

    return solucion, problema.costo(solucion),tiempo_final - tiempo_inicial


if __name__ == "__main__":

    #################################################################################################
    #                          20 PUNTOS
    #################################################################################################
    # Modifica los valores de la función siguiente (o el parámetro del algo_genetico)
    # buscando que el algoritmo encuentre SIEMPRE una solución óptima, utilizando el menor tiempo
    # posible en promedio. Realiza esto para las 8, 16 y 32 reinas.
    #   -- ¿Cuales son en cada caso los mejores valores (escribelos abajo de esta lines)
    #
    #       * 8 reinas *
    #
    #       - probabilidad de mutacion 0.001 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 0.32
    #       Tiempo promedio = 0.0151285076141
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((4, 0, 3, 5, 7, 1, 6, 2), 0, 0.015546083450317383)
    #
    #       - probabilidad de mutacion 0.01 - poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 0.44
    #       Tiempo promedio = 0.0155563855171
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((5, 2, 4, 6, 0, 3, 1, 7), 0, 0.016511201858520508)
    #
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 0.24
    #       Tiempo promedio = 0.0153913903236
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((6, 1, 5, 2, 0, 3, 7, 4), 0, 0.01609206199645996)
    #
    #       * 16 reinas *
    #
    #       - probabilidad de mutacion 0.001 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 3.01
    #       Tiempo promedio = 0.0438059258461
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       ((8, 15, 4, 12, 14, 11, 3, 5, 9, 1, 13, 0, 2, 7, 10, 6), 1, 0.04398298263549805)
    #
    #       - probabilidad de mutacion 0.01 - poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 3.13
    #       Tiempo promedio = 0.0447863960266
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((2, 6, 11, 1, 10, 15, 9, 4, 0, 12, 14, 7, 13, 3, 5, 8), 1, 0.043958187103271484)
    #
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 2.85
    #       Tiempo promedio = 0.0458542752266
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((10, 12, 7, 15, 4, 1, 5, 0, 8, 3, 11, 14, 2, 6, 9, 13), 2, 0.04676985740661621)
    #
    #       * 32 reinas *
    #
    #       - probabilidad de mutacion 0.001 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 9.35
    #       Tiempo promedio = 0.157243328094
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((16, 23, 4, 27, 15, 24, 12, 21, 26, 29, 25, 1, 11, 30, 10, 18, 28, 0, 17, 7, 6, 19, 3, 31, 8, 14, 13, 20, 9, 2, 22, 5), 6, 0.15579605102539062)
    #
    #       - probabilidad de mutacion 0.01 - poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 9.48
    #       Tiempo promedio = 0.158712005615
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((18, 21, 8, 10, 13, 0, 28, 26, 19, 16, 22, 25, 11, 3, 31, 7, 14, 2, 29, 5, 23, 17, 12, 6, 15, 1, 20, 4, 24, 30, 27, 9), 6, 0.1739211082458496)
    #
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 9.21
    #       Tiempo promedio = 0.161803388596
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((2, 14, 8, 11, 24, 20, 1, 28, 9, 3, 27, 21, 30, 16, 10, 31, 22, 15, 23, 4, 19, 7, 18, 26, 6, 29, 5, 0, 25, 13, 17, 12), 6, 0.16707301139831543)
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun tu experiencia
    #
    #       * 8 reinas *
    #
    #       En el caso de las 8 reinas la siguiente configuracion tuvo buena aptitud y promedio a comparacion de las otras
    #       a mi criterio claro entonces para el caso de las 8 reinas opto por esta configuracion.
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       * 16 reinas *
    #
    #       En el caso de las 16 reinas la siguiente configuracion tuvo buena aptitud y promedio a comparacion de las otras
    #       a mi criterio claro entonces para el caso de las 16 reinas opto por esta configuracion.
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       * 32 reinas *
    #
    #       En el caso de las 32 reinas la siguiente configuracion tuvo buena aptitud y promedio a comparacion de las otras
    #       a mi criterio claro entonces para el caso de las 32 reinas opto por esta configuracion.
    #        - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Para realizar estas conclusiones me enfoque principalmente en la aptitud promedio ya que pienso que el tiempo
    #       aqui es insignificante. Me he llevado la sorpresa que la mejor configuracion a mi parecer ha sido la siguiente
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #       Entonces mi regla seria utilizar principalmente esta probabilidad de mutacion.

    """"

    ma = 0
    mt = 0
    it = 100
    for x in xrange(1,it):
        solucion = prueba_genetico_nreinas(algo_genetico = GeneticoPermutaciones1(0.05),
        problema = nreinas.ProblemaNreinas(32),
        n_poblacion = 50,
        n_generaciones = 10)
        temp1 = float(solucion[1])
        temp2 = float(solucion[2])
        ma += temp1
        mt += temp2

        if x == 1:
            si = solucion
        if solucion[1] < si[1]:
            si = solucion

    print 'Aptitud promedio'
    print ma/it
    print 'Tiempo promedio'
    print mt/it
    print 'Super Individuo'
    print si

     """


    #################################################################################################
    #                          20 PUNTOS
    #################################################################################################
    # Modifica los valores de la función siguiente (o los posibles parámetro del algo_genetico)
    # buscando que el algoritmo encuentre SIEMPRE una solución óptima, utilizando el menor tiempo
    # posible en promedio. Realiza esto para las 8, 16 y 32 reinas.
    #   -- ¿Cuales son en cada caso los mejores valores (escribelos abajo de esta lines)
    #
    #       * 8 reinas *
    #
    #       - probabilidad de mutacion 0.001 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 0.7
    #       Tiempo promedio = 0.0266610383987
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((4, 2, 7, 3, 6, 0, 5, 1), 0, 0.026213884353637695)
    #
    #       - probabilidad de mutacion 0.01 - poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 0.68
    #       Tiempo promedio = 0.0257033824921
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((3, 7, 0, 2, 5, 1, 6, 4), 0, 0.0272829532623291)
    #
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 0.56
    #       Tiempo promedio = 0.0260768437386
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((0, 6, 4, 7, 1, 3, 5, 2), 0, 0.026152849197387695)
    #
    #       * 16 reinas *
    #
    #       - probabilidad de mutacion 0.001 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 3.51
    #       Tiempo promedio = 0.0788898468018
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((5, 0, 1, 9, 6, 12, 15, 11, 3, 7, 10, 14, 2, 13, 8, 4), 2, 0.07773494720458984)
    #
    #       - probabilidad de mutacion 0.01 - poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 3.49
    #       Tiempo promedio = 0.0787416601181
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((6, 14, 7, 4, 1, 13, 2, 10, 8, 12, 3, 9, 11, 15, 5, 0), 2, 0.07862496376037598)
    #
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 3.49
    #       Tiempo promedio = 0.0808884358406
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       ((5, 1, 10, 0, 14, 11, 8, 3, 7, 12, 4, 15, 13, 6, 9, 2), 1, 0.08501815795898438)
    #
    #       * 32 reinas *
    #
    #       - probabilidad de mutacion 0.001 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 10.28
    #       Tiempo promedio = 0.281864349842
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((6, 8, 14, 1, 10, 20, 11, 16, 3, 17, 28, 30, 29, 22, 23, 19, 27, 13, 2, 21, 0, 12, 9, 5, 24, 4, 7, 26, 31, 18, 15, 25), 7, 0.2836270332336426)
    #
    #       - probabilidad de mutacion 0.01 - poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 10.05
    #       Tiempo promedio = 0.280721604824
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((22, 4, 14, 29, 24, 12, 10, 1, 19, 26, 0, 9, 31, 28, 7, 23, 17, 13, 27, 16, 5, 30, 21, 25, 6, 11, 18, 15, 3, 20, 8, 2), 7, 0.28223395347595215)
    #
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Aptitud promedio = 9.91
    #       Tiempo promedio = 0.286687326431
    #       Caracteristicas del super individuo mostrado abajo = Cromosoma + aptitud + tiempo
    #       Super Individuo = ((14, 3, 13, 6, 20, 1, 31, 26, 29, 18, 9, 15, 5, 0, 4, 8, 22, 30, 28, 11, 21, 10, 12, 17, 7, 25, 2, 24, 16, 27, 19, 23), 6, 0.29471898078918457)
    #
    #   -- ¿Que reglas podrías establecer para asignar valores segun tu experiencia? Escribelo aqui
    #   abajo, utilizando tanto espacio como consideres necesario.
    #
    #       * 8 reinas *
    #
    #       En el caso de las 8 reinas la siguiente configuracion tuvo buena aptitud y promedio a comparacion de las otras
    #       a mi criterio claro entonces para el caso de las 8 reinas opto por esta configuracion.
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       * 16 reinas *
    #
    #       En el caso de las 16 reinas dos configuraciones tuvieron la misma media de aptitud
    #       entonces el otro criterio a considerar seria el tiempo que no toma tanta significancia a mi parecer en este caso
    #       particular entonces opto por la siguiente configuracion
    #       - probabilidad de mutacion 0.01 - poblacion 50 - generaciones 10 -
    #
    #       * 32 reinas *
    #
    #       En el caso de las 32 reinas la siguiente configuracion tuvo buena aptitud y promedio a comparacion de las otras
    #       a mi criterio claro entonces para el caso de las 32 reinas opto por esta configuracion.
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    #       Para realizar estas conclusiones me enfoque principalmente en la aptitud promedio ya que pienso que el tiempo
    #       aqui es insignificante. Me he llevado la sorpresa que la mejor configuracion a mi parecer ha sido la siguiente
    #       - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #       Entonces mi regla seria utilizar principalmente esta probabilidad de mutacion.
    #
    #       Conclusion final
    #        Utiliza esta configuracion varia los parametros de poblacion y generacion pero permanece con la probabilidad de
    #        mutacion de 0.05.
    #        - probabilidad de mutacion 0.05 - Poblacion 50 - generaciones 10 -
    #
    # Recuerda de quitar los comentarios de las lineas siguientes:

    """"

    ma = 0
    mt = 0
    it = 100
    for x in xrange(1,it):
        solucion = prueba_genetico_nreinas(algo_genetico = GeneticoPermutaciones2(0.05),
        problema = nreinas.ProblemaNreinas(32),
        n_poblacion = 50,
        n_generaciones = 10)
        temp1 = float(solucion[1])
        temp2 = float(solucion[2])
        ma += temp1
        mt += temp2

        if x == 1:
            si = solucion
        if solucion[1] < si[1]:
            si = solucion

    print 'Aptitud promedio'
    print ma/it
    print 'Tiempo promedio'
    print mt/it
    print 'Super Individuo'
    print si

    """

    """"

    solucion = prueba_genetico_nreinas(algo_genetico=GeneticoPermutaciones1(0.05),
                                            problema=nreinas.ProblemaNreinas(16),
                                            n_poblacion=50,
                                            n_generaciones=10)
    print solucion

    """

    solucion = prueba_genetico_nreinas(algo_genetico=GeneticoPermutaciones2(0.05),
                                            problema=nreinas.ProblemaNreinas(16),
                                            n_poblacion=50,
                                            n_generaciones=10)
    print solucion