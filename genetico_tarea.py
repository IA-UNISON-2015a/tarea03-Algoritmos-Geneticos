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
        #Ya inicializa la población
        super().__init__(problema, n_población)
        #porcentaje de cruza -->.6
        #seleccion: elitista o otro
        #
        # ------ IMPLEMENTA AQUI TU CÓDIGO -----------------------------------
        #
        self.nombre = 'Erick Fernando Lopez Fimbres'
        self.prob_muta=prob_muta
        
        #iba a meter como parametro la probabilidad de cuza pero la use local.
        
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
        
        #convertimos a cadenas los estados
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
        
        #regresamos a su forma normal
        dominio=list(range(0,len(cadena)))
        estado=[]
        #print(cadena)
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
        #Adaptacion exponencial
        K=1
        return math.exp(-K*self.problema.costo(self.cadena_a_estado(individuo)))
        raise NotImplementedError("¡Este metodo debe ser implementado!")
    
    def torneoArtesMarciales(self):
        #Elegimos un la mitad de la poblacion aleatoriamente para sacar a
        #los dos mejores
        tamaño=math.ceil(self.n_población/2)
        if tamaño%2==1:
            tamaño+=1
        competidores = list(self.población)
        ganadores=[]
        #elegimos al azar a los competidores
        for i in range(tamaño):
            c1=random.randint(0,len(competidores)-1)
            lista=list(competidores[c1])
            competidores.remove(competidores[c1])
            lista.append(c1)
            ganadores.append(lista)
        
        #hacemos que se enfrenten por varias rondas
        while(len(ganadores) > 2):
            ronda=len(ganadores)
            for x in range(ronda//2):
                if ganadores[x][0] >= ganadores[x+1][0]:
                    ganadores.remove(ganadores[x+1])
                else:
                    ganadores.remove(ganadores[x])
                    
        #solo quedan los ganadores (los mas aptos)
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
        
        #Cruza uniforme
        Pc = 0.5
        hijo=[]
        #empezamos a mezclar cromosomas de ambos padres
        for x in range(len(cadena1)):
            if(random.random()<= Pc):
                hijo.append(cadena1[x])
            else:
                hijo.append(cadena2[x])
        
        #el resultado de la cruza
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
        
        #por la manera en que hice la cadena 
        #la mutacion se me ocurrio hacerla así
        for individuo in individuos:
            for i in range(len(individuo)):
                if random.random() < self.prob_muta:
                    #puede mutar cualquier cromosoma
                    i=random.randint(0,len(individuo)-1)
                    #el cromosoma solo puede toar valores menores a su posicio
                    #por la estructura de a cadena
                    v=random.randint(0,len(individuo)-1-i)
                    #mutamos al individuo
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
        
        #enfrentamos a los hijos con los padres y los mejores se quedan
        for x in range(len(self.población)):
            if reemplazo[x][0] > self.población[x][0]:
                nuevaG.append(reemplazo[x])
            else:
                nuevaG.append(self.población[x])
        self.población=nuevaG[:]
        
        #esta forma de abajo no sirvio muy bien lo cual consistia en 
        #conservar a un cuarto de la población
        """
        part=math.ceil(len(self.población)/4)
        self.población.sort(reverse=True)
        veteranos=self.población[:part]
        
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
