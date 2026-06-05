'''
Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais; 
Em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l;
O valor da gasolina é de 5 reais o litro. 

O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, 

crie três funções nas quais: 
a 1ª função calcule os gastos com hotel (gasto_hotel), 
a 2ª calcule os gastos com a gasolina (gasto_gasolina) e 
a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
'''
dias = int(input('Insira o número de dias: '))

cidade = (input('Insira a cidade de destino: ')).lower().strip()

volta = (input('Viagem de volta? ')).lower().strip()

distancias = [850, 800, 300, 550]

passeio_alimentacao = [200, 400, 250, 300]

def gasto_hotel(dias_inseridos):
    hotel = dias*150
    return hotel

#fazer para a cidade inserida pelo usuario
def gasto_gasolina(lista_distancias, volta_inserida):
    if cidade == 'salvador':
        d = distancias[0]
    
    elif cidade == 'fortaleza':
        d = distancias[1]
    
    elif cidade == 'natal':
        d = distancias[2]
    
    elif cidade == 'aracaju':
        d = distancias[3]

    l = d/14
    gasolina = 5*l

    if volta == 'sim':
        gasolina = gasolina*2

    return gasolina

#fazer para o numero de dias inserido pelo usuario
def gasto_passeio(dias_inseridos, lista_passeio):
    if cidade == 'salvador':
        passeio = passeio_alimentacao[0]*dias
    
    if cidade == 'fortaleza':
        passeio = passeio_alimentacao[1]*dias
    
    if cidade == 'natal':
        passeio = passeio_alimentacao[2]*dias
    
    if cidade == 'aracaju':
        passeio = passeio_alimentacao[3]*dias
    
    return passeio

hotel = gasto_hotel(dias)
gasolina = gasto_gasolina(cidade, volta)
passeio = gasto_passeio(dias, cidade)

print(f'\n======GASTOS TOTAIS=====\nTotal hotel\tR${hotel}\nTotal gasolina\tR${gasolina:.2f}\nTotal passeios\tR${passeio}')