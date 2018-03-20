'''
Created on 20 de mar de 2018

@author: karol
'''

from classes.crossover import *
from classes.populacao import *
from scripts_para_popular.populacao_criar import *


def crossover_criar(populacao_para_crossover, numero_cruzamentos):
    crossover = Crossover(populacao_para_crossover, numero_cruzamentos)    
    return crossover

