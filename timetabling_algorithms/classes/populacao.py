'''
Created on 19 de mar de 2018

@author: karol
'''

class Populacao(object):
    
    def __init__(self, numero_individuos, conjunto_individuo, fitness_populacao):
        self.numero_individuos = numero_individuos
        self.conjunto_individuo = conjunto_individuo
        self.fitness_populacao = fitness_populacao