'''
Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
'''

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

soma = [sum(lista_de_listas[i]) for i in range(len(lista_de_listas))]

print(soma)