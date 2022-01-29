import random
from time import sleep
pc = random.randint(1,5)
vc = int(input('De 1 a 5 adivinhe o numero:'))
print('_-'*30)
print('Processando...')
sleep(2)#faz ele esperar 3 segundos
if pc==vc:
    print('O número é {}, você acertou!'.format(pc))
else:
    print('Voce errou, o número é {} e não o {}'.format(pc,vc))
print('_-'*30)