'''
Você foi contratado(a) como cientista de dados de uma associação de skate. 
Para analisar as notas de skatistas em competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. 
Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. 
Retorne a média para apresentar o texto:

"Nota da manobra: [media]"
'''

notas = []

for i in range(1,6):
    n = float(input('Insira a nota: '))
    notas.append(n)

def pontuacao_skate(lista):
    maior = 0
    #Ver o maior elemento da lista(pode-se usar a função max())
    for elemento in lista:
        if elemento>maior:
            maior = elemento
    
    #Ver o menor elemento da lista(pode-se usar a função min())
    menor = maior
    for elemento in lista:
        if elemento<menor:
            menor = elemento
    
    lista.remove(maior)
    lista.remove(menor)

    media = float(sum(lista)/len(lista))

    return media

media_final = pontuacao_skate(notas)

print('Nota da manobra:',media_final)