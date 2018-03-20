'''
Created on 19 de mar de 2018

@author: karol
'''

from classes.populacao import *
from scripts_para_popular.individuo_criar import *
from classes import populacao

def populacao_criar(numero_individuos):
    conjunto_populacao = [individuo_criar() for numero in range(numero_individuos)]    
    populacao = Populacao(numero_individuos, conjunto_populacao, 0)
    return populacao

