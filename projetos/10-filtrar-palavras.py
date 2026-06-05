'''
Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). 
Sua líder requisitou que você criasse um trecho de código que 
    recebe uma frase digitada pela pessoa usuária
    filtre apenas as palavras com tamanho maior ou igual a 5
    exibindo-as em uma lista. 

Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

Dica: utilize as funções lambda e filter() para filtrar essas palavras. 

Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e 
filtra um iterável de acordo com a função. 
Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.
'''
frase = input('Insira uma frase:\n')

frase = frase.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')

palavra = frase.split()

maior_5 = filter(lambda palavra: len(palavra) >= 5 , palavra) #map devolve bool, enquanto filter devolve o termo

maior_5 = list(maior_5)

print(maior_5)
