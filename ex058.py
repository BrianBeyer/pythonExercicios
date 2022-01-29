import random
from time import sleep
pc = random.randint(0,10)
print('_-'*30)
acertou = False
palpite = 0
while not acertou:
    vc = int(input('De 1 a 10 adivinhe o numero:'))
    palpite +=1
    if pc == vc:
        acertou = True
    else:
        if vc < pc:
            print('Mais... tente de novo!')
            print(' ')
        elif vc > pc:
            print('Menos...tente de novo!')
            print(' ')
print('Acertou com {} tentativas.'.format(palpite))

print('_-'*30)
