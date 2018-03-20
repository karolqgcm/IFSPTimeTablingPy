'''
Created on 20 de mar de 2018

@author: karol
'''

import random
from classes.populacao import *
from classes.individuo import *

class Crossover:
    
    def __init__(self, populacao, numero_cruzamentos): 
        self.populacao = populacao
        self.numero_cruzamentos = numero_cruzamentos
    
    def selecionar_genitores(self):
        mae = random.choice(self.populacao.conjunto_individuo) 
        pai = random.choice(self.populacao.conjunto_individuo)
        if (mae != pai):
            return mae, pai
        elif (len(self.populacao.conjunto_individuo)<=1):
            print("Indivíduos insuficientes para cruzamento")
        else:
            self.selecionar_genitores()
        
    
    def cruzamento(self):
        genitores = self.selecionar_genitores()
        mae = genitores[0]
        pai = genitores[1]
        filho = Individuo(mae.gene1, pai.gene2, 0)
        self.populacao.append(filho)
   
        
                