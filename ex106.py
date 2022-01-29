from time import sleep

c = ('\033[m',# 0 sem cor
     '\033[0;30;41m',# 1 vermelho
     '\033[030;42m', # 2 verde
     '\033[030;43m', # 3 amarelo
     '\033[030;44m', # 4 azul
     '\033[030;45m', # 5roxo
     '\033[7;30m'    # 6 branco
     );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[3],end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[2],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')# para limpar as cores
    sleep(1)

comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 2)# numero para a cor
    comando = str(input(('Função ou Biblioteca > ')))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo!', 1)