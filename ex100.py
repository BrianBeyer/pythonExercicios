import random
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista:',end='')
    for cont in range(0, 5):
        n = random.randint(1,10)
        lista.append(n)
        print(n,end=' ')
        sleep(0.9)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor%2 == 0:
            soma += valor
    print('')
    print(f'A soma dos valores pares de {lista} é {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)
