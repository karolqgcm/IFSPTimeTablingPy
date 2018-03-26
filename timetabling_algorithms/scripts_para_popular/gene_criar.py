'''
Created on 14 de mar de 2018

@author: karol
'''

import random
from classes.gene_dia import *

dict_professor_disciplina = [
    {"Nelson - SEG"},
    {"Luciana - PI2"}, 
    {"Mario - TOP"},
    {"Henrique - DW2"}    
]


def gene_criar():
    gene_novo = GeneDia(random.choice(dict_professor_disciplina))
    #gene_novo = Gene("Fulano - BLA")
    return gene_novo

