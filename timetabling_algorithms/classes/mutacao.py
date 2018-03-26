'''
Created on 22 de mar de 2018

@author: karol
'''

import random
from scripts_para_popular.gene_criar import *
from classes.individuo_dia import *

class Mutacao:
    def __init__(self, populacao_a_receber_mutacao, conjunto_de_genes_para_mutacao, porcentagem_de_mutacao):
        self.populacao_a_receber_mutacao = populacao_a_receber_mutacao
        self.conjunto_de_genes_para_mutacao = conjunto_de_genes_para_mutacao
        self.porcentagem_de_mutacao = porcentagem_de_mutacao
        
    def mutacao_dia(self):
        for individuo_dia in self.populacao_a_receber_mutacao:
            if random.randint(0,100) <= self.porcentagem_de_mutacao:
                    gene_mutado = gene_criar()
                    individuo_a_ser_mutado = random.choice(self.populacao_a_receber_mutacao)
                    individuo_a_ser_mutado.gene2 = gene_mutado
        