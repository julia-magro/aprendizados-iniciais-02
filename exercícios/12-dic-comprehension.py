'''
Crie um dicionário usando o dict comprehension em que: 
    chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os 
    valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].
'''
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesas = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dic = {meses[i] : despesas[i] for i in range(len(meses and despesas))}

print (dic)