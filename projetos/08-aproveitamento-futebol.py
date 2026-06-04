'''
Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. 
Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. 
A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

    Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. 
    Caso seja igual, o time empatou e se for menor, o time perdeu. 
    Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"
'''

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(lista_marcados,lista_sofridos):
    pontuacao = 0
    for n in lista_marcados and lista_sofridos:
        if lista_marcados[n]>lista_sofridos[n]:
            #venceu
            pontuacao += 3
        
        elif lista_marcados[n]==lista_sofridos[n]:
            #empate
            pontuacao += 1
        
        else:
            #derrota
            pontuacao += 0
    
    aproveitamento = pontuacao/15

    return pontuacao, aproveitamento

pontuacao, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)

print(f'A pontuação do time foi de {pontuacao} e seu aproveitamento foi de {aproveitamento:.2f}%')




