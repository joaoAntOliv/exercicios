'''Escreva um programa que receba uma lista de números digitados pelo usuário e 
exiba o maior número e o menor número da lista.'''
# to muito ruim, n me julgue

lista = [

]


while True:

    adicionar = int(input('Adicionar a lista:(digite 0 para parar) '))

    if adicionar == 0:
        break

    try:
        num = float(adicionar)
        lista.append(num)
    except ValueError:
        print('Digite uma resposta válida')

    if len(lista) > 0:
        menor = min(lista)
        maior = max(lista)
    else:
        print('Nenhum número digitado')

    print(maior)