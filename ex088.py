import random
from time import sleep
lista = []
jogos = list()
print('-'*20)
print('MEGA SENA')
print('-'*20)
quant = int(input('Quantos jogos quer que eu sorteie?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
            if cont == 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-='*3,f'Sorteando {quant} Jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< Boa sorte >', '-='*5)



'''print('-'*20)
print('MEGA SENA')
print('-'*20)
j = []
jogos = int(input('Quantos jogos você quer sortear?'))
for c in range(1,jogos+1):
    for b in range(1,7):
        j.append(random.randint(1,60))
    print(f'Jogo {c}:',end=' ')
    print(sorted(j))
    j.clear()
print('-----Boa sorte-----')'''