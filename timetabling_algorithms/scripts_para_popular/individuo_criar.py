'''
Created on 19 de mar de 2018

@author: karol
'''

from classes.individuo_dia import *
from scripts_para_popular.gene_criar import *

def individuo_criar():
    gene1 = gene_criar()
    gene2 = gene_criar()
    fitness_individuo = 0
    individuo_novo = IndividuoDia(gene1,gene2,fitness_individuo)
    print(individuo_novo.gene1.professor_disciplina, individuo_novo.gene2.professor_disciplina, individuo_novo.fitness_individuo)
    return individuo_novo

