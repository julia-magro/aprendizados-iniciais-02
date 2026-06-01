'''
Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

 Dica: use a função pow() da biblioteca math
'''
from math import pow

n1 = int(input('Insira o número que será a base: '))

n2 = int(input('Insira o número que será o expoente: '))

r = pow(n1,n2)

print(f'Resultado: {r}')