# -*- coding: utf-8 -*-
"""Exercicio 05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10q9jMedwzKaDRKGAsH310uiqxLhMxOZr
"""

n_1 = float(input('A primeira nota foi de '))
n_2 = float(input('A segunda nota foi de '))

notas = n_1 + n_2
media = notas / 2

if media >= 7.0 and media <= 9.9:
  print(f'Você foi aprovado com {media}.')

elif media == 10.0:
  print(f'Você foi aprovado com distinção!')

else:
  print(f'Você foi reprovado com {media}.')