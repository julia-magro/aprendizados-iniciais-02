'''
Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3.
'''
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos(lista1):
    mult = []
    for n in lista1:
        if n%3==0:
            mult.append(n)

    return mult

mult_3 = multiplos(lista)

print(mult_3)
