import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
import random
print('''Escolha:
[0] PEDRA
[1] PAPEl
[2] TESOURA''')
jogador = int(input('Qual sua jogada?'))
print("JO")
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('=-'*10)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('=-'*10)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada invalida!')

elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada invalida!')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida!')
