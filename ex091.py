import random
from operator import itemgetter
from time import sleep
jogo = { 'jogador1': random.randint(1,6),
'jogador2': random.randint(1,6),
'jogador3': random.randint(1,6),
'jogador4': random.randint(1,6),}
ranking = list()#para criar a ordem
print('Valores sorteados')
for k, v in jogo.items():
     print(f'O {k} tirou {v} no dado')
     sleep(0.5)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)#vai pegar a posiçao 1 que é o rondom e colocar em ordem, reverse para colocar do maior para o menor
print('-='*15)
for i, v in enumerate(ranking):
     print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
     sleep(0.5)


