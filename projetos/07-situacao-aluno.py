'''
 Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, 
 você precisa criar uma função que receba uma lista de 4 notas e retorne:

    maior nota
    menor nota
    média
    situação (Aprovado(a) ou Reprovado(a))

Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
'''
notas = []

for i in range(1,5):
    nota = float(input(f'Insira a {i}° nota: '))
    notas.append(nota)

def buzz(lista):
    situacao = 'reprovado'
    maior = max(lista)
    menor = min(lista)
    media = sum(lista)/len(lista)
    if media>=6:
        situacao = 'aprovado'
    return maior, menor, media, situacao

maior, menor, media, situacao = buzz(notas)

print(f'O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}')