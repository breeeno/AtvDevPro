# -*- coding: utf-8 -*-
"""Exercicio 01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yxrb3qhy5iTnRT97aM5dQAYI2KSTBfOc
"""

linha1 = str(input('Digite uma frase: '))
linha2 = str(input('Digite uma frase: '))

print(linha1), len(linha1)
print(linha2), len(linha2)

if linha1 == linha2:
  print('As sentenças são iguais')
elif linha1 != linha2:
  print('As sentenças são diferentes')

if len(linha1) == len(linha2):
  print('A quantidade de caractéres é iguais')
elif len(linha1) != len(linha2):
  print('A quantidade de caractéres são diferentes')