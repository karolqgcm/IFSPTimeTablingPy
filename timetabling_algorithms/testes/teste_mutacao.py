'''
Created on 22 de mar de 2018

@author: karol
'''

import unittest
from scripts_para_popular.mutacao_criar import *
from classes.gene_dia import *
from scripts_para_popular.populacao_criar import *
from testes.teste_populacao import populacao_a_ser_testada

populacao_a_ser_testada = Populacao(2)
mutacao_a_ser_testada = Mutacao()
class TestarMutacao(unittest.TestCase):
    def testar_mutacao_individuo_dia(self):
        pass