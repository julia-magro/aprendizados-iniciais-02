'''
Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. 
Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
'''

from random import randrange

qtd = int(input('Insira o número total de participantes: '))

sorteado = randrange(qtd+1)

print('O participante sorteado é o:',sorteado)