'''
Created on 12 de mar de 2018

@author: karol
'''
import unittest
from classes.gene_dia import *
from scripts_para_popular.gene_criar import *

gene_a_ser_testado = gene_criar()

class TestarGene(unittest.TestCase):   
     
    def testar_vazio(self):
        self.assertNotEqual(len(gene_a_ser_testado.professor_disciplina), 0, "Gene está vazio")
    
    def testar_se_esta_no_conjunto(self):
        self.assertIn(gene_a_ser_testado.professor_disciplina, dict_professor_disciplina, "Gene está no conjunto")