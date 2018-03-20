'''
Created on 19 de mar de 2018

@author: karol
'''

import unittest
from classes.populacao import *
from scripts_para_popular.populacao_criar import *

numero_individuos = 2
populacao_a_ser_testada = populacao_criar(numero_individuos)
class TestarPopulacao(unittest.TestCase):
    def teste_numero_individuo(self):
        self.assertEqual(len(populacao_a_ser_testada.conjunto_individuo), numero_individuos, "O número de indivíduos está correto")
        