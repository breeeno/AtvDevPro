# -*- coding: utf-8 -*-
"""Exercicio 16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1riJMCMike9x9wKa1StDNuvqZwHicFd4I
"""

salarios = [220, 330, 450, 480, 500, 602, 750, 840, 950, 1010]
contagem_salarios = [0] * 9
for salario in salarios:
  indice = salario // 100 -2
  indice_maximo = len(contagem_salarios) -1
  indice = min(indice, indice_maximo)
  contagem_salarios[indice] += 1
  
  
print(contagem_salarios)