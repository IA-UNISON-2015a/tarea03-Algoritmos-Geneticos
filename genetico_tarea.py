#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
genetico_tarea.py
-----------------

En este módulo vas a desarrollar tu propio algoritmo
genético para resolver problemas de permutaciones

"""
import math
import random
import genetico

__author__ = 'Erick Fernando López Fimbres'


class GeneticoPermutacionesPropio(genetico.Genetico):
    """
    Clase con un algoritmo genético adaptado a problemas de permutaciones

    """
    def __init__(self, problema, n_población,prob_muta=0.01):
        """
        Aqui puedes poner algunos de los parámetros
        que quieras utilizar en tu clase

        Para esta tarea vamos a cambiar la forma de representación
        para que se puedan utilizar operadores clásicos (esto implica
        reescribir los métodos estáticos cadena_a_estado y
        estado_a_cadena).

        """
        self.nombre = 'Erick Fernando Lopez Fimbres'
        self.prob_muta=prob_muta
        #Ya inicializa la población
        super().__init__(problema, n_población)
        #porcentaje de cruza -->.6
        #seleccion: elitista o otro
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        #
        #print("La poblacion es: ")
        #print(self.población)
        #prob_muta
        #self.p_muta=p_muta
        #self.p_cruza=p_cruza
        #self.tipo_selección=tipo_seleccion
        
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
        dominio=list(range(0,len(estado)))
        cadena=[]
        for x in range(len(estado)):
            cadena.append(dominio.index(estado[x]))
            dominio.remove(estado[x])
        
        return cadena
        raise NotImplementedError("¡Este metodo debe ser implementado!")

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
        dominio=list(range(0,len(cadena)))
        estado=[]
        print(cadena)
        for x in range(0,len(cadena)):
            
            estado.append(dominio[cadena[x]])
            dominio.remove(dominio[cadena[x]])
    
        return tuple(estado)
        raise NotImplementedError("¡Este metodo debe ser implementado!")

        
    def adaptación(self, individuo):
        """
        Calcula la adaptación de un individuo al medio, mientras más adaptado
        mejor, mayor costo, menor adaptción.

        @param individuo: Una lista de cromosomas
        @return un número con la adaptación del individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        K=1
        return math.exp(-K*self.problema.costo(self.cadena_a_estado(individuo)))
        raise NotImplementedError("¡Este metodo debe ser implementado!")
    
    def torneoArtesMarciales(self):
        #print("torneoo...")
        tamaño=4
        competidores = list(self.población)
        ganadores=[]
        #elegimos al azar varios competidores
        
        for i in range(tamaño):
            c1=random.randint(0,len(competidores)-1)
            lista=list(competidores[c1])
            competidores.remove(competidores[c1])
            lista.append(c1)
            ganadores.append(lista)
        #print("....", ganadores)
        #while(len(ganadores) > 2):
        for x in range(len(ganadores)-2):
            if ganadores[x][0] >= ganadores[x+1][0]:
                ganadores.remove(ganadores[x+1])
            else:
                ganadores.remove(ganadores[x])
                
        #print("Los ganadores son",ganadores[0],ganadores[1])
        return ganadores[0][2],ganadores[1][2]
    def selección(self):
        """
        Seleccion de estados mediante método diferente a la ruleta

        @return: Una lista con pares de indices de los individuo que se van
                 a cruzar

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        
        return [self.torneoArtesMarciales()
                for _ in range(self.n_población)]

        raise NotImplementedError("¡Este metodo debe ser implementado!")

    def cruza_individual(self, cadena1, cadena2):
        """
        @param cadena1: Una tupla con un individuo
        @param cadena2: Una tupla con otro individuo
        @return: Un individuo

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO ----------------------------------
        #
        
        # Position-based Crossover para permutaciones
        #Cruza uniforme
        Pc = 0.4
        hijo=[]
        for x in range(len(cadena1)):
            if(random.random()<= Pc):
                hijo.append(cadena1[x])
            else:
                hijo.append(cadena2[x])
        
        return hijo
        raise NotImplementedError("¡Este metodo debe ser implementado!")

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
        for individuo in individuos:
            for i in range(len(individuo)):
                if random.random() < self.prob_muta:
                    i=random.randint(0,len(individuo)-1)
                    v=random.randint(0,len(individuo)-1-i)
                    individuo[i]=v
        return None
        raise NotImplementedError("¡Este metodo debe ser implementado!")

    def reemplazo_generacional(self, individuos):
        """
        Realiza el reemplazo generacional diferente al elitismo

        @param individuos: Una lista de cromosomas de hijos que pueden
                           usarse en el reemplazo
        @return: None (todo lo cambia internamente)

        Por default usamos solo el elitismo de conservar al mejor, solo si es
        mejor que lo que hemos encontrado hasta el momento.

        """
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO --------------------------------
        #
        nuevaG=list()
        reemplazo = [(self.adaptación(individuo), individuo)
                     for individuo in individuos]
        reemplazo.sort(reverse=True)
        self.población.sort(reverse=True)
        
        for x in range(len(self.población)):
            if reemplazo[x][0] > self.población[x][0]:
                nuevaG.append(reemplazo[x])
            else:
                nuevaG.append(self.población[x])
        self.población=nuevaG[:]
        
        """
        part=math.ceil(len(self.población)/4)
        self.población.sort(reverse=True)
        veteranos=self.población[:part]
        print("veteranos",veteranos)
        
        reemplazo = [(self.adaptación(individuo), individuo)
                     for individuo in individuos]
        
        reemplazo.sort(reverse=True)
        self.población = veteranos[:] + reemplazo[part:self.n_población]
        """
if __name__ == "__main__":
    # Un objeto genético con permutaciones con una población de
    # 10 individuos y una probabilidad de mutacion de 0.1
    g_propio = GeneticoPermutacionesPropio(genetico.ProblemaTonto(10), 10)
    genetico.prueba(g_propio)
