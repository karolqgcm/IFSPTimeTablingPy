'''
Created on 9 de mar de 2018

@author: karol
'''

from classes import individuo
from scripts_para_popular.individuo_criar import *
import unittest

individuo_a_ser_testado = individuo_criar()

class TestarCriarIndividuo(unittest.TestCase):
    def teste_individuo_fitness_nao_negativo(self):
        self.assertGreaterEqual(individuo_a_ser_testado.fitness_individuo, 0, "Fitness do indivíduo não é negativo")
    