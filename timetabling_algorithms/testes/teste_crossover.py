'''
Created on 20 de mar de 2018

@author: karol
'''
import unittest
from classes.crossover import *
from scripts_para_popular.crossover_criar import *
from scripts_para_popular.populacao_criar import *

populacao_para_crossover = populacao_criar(1)
crossover_a_ser_testado = crossover_criar(populacao_para_crossover, 1)

class Testar_Crossover(unittest.TestCase):
    def testar_genitores_iguais(self):
        self.assertNotEqual(crossover_a_ser_testado.selecionar_genitores()[0], crossover_a_ser_testado.selecionar_genitores()[1], "Genitores são os mesmos")