'''
Created on 22 de mar de 2018

@author: karol
'''

import random
from classes.mutacao import *
from scripts_para_popular.populacao_criar import *
from scripts_para_popular.gene_criar import *


populacao_a_ser_mutada = populacao_criar(4)

def mutacao_criar(populacao_a_receber_mutacao, conjunto_de_genes_para_mutacao, porcentagem_de_mutacao):
    mutacao = Mutacao(populacao_a_receber_mutacao, conjunto_de_genes_para_mutacao, porcentagem_de_mutacao)
    return mutacao

mutacao = mutacao_criar(populacao_a_ser_mutada.conjunto_individuo, dict_professor_disciplina, 50)
mutacao.mutacao_dia()

