'''
Escreva um código que lê a lista abaixo e faça:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

    A leitura do tamanho da lista
    A leitura do maior e menor valor
    A soma dos valores da lista

Ao final exiba uma mensagem dizendo:

"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. 
A soma dos valores presentes nela é igual a [soma]"
'''

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

soma = sum(lista)
tam = len(lista)
maior = 0
menor = 100

for n in lista:
    if n>maior:
        maior = n
    
    if n<menor:
        menor = n

print(f'A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}.\nA soma dos valores presentes nela é igual a {soma}')