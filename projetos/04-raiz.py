'''
Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. 
A lista é a seguinte:

numeros = [2, 8, 15, 23, 91, 112, 256]

No final, informe quais números possuem raízes inteiras e seus respectivos valores.
'''
from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

for n in numeros:
    r = sqrt(n)
    if r%1 == 0:
        print(f'O número {n} possui raiz inteira (raiz = {r})')


