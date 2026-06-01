'''
1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.

2. Escreva um código para importar a biblioteca numpy com o alias np.

3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
'''

#pip install matplotlib==3.7.1

import numpy as np

from random import choice

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

n = choice(lista)

print(n)


