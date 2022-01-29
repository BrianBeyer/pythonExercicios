partidas = []
jogador = {}
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)# recebe a soma de partidas
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N!')
    if resp == 'N':
        break
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for k, v in enumerate(time):# ja que time é uma lista
    print(f'{k:>3} ',end='')#3 caracteres centralizado a direita
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dado de qual jogador? (999 finaliza.) '))
    if busca == 999:
        break
    if busca >= len(time): #se a busca for maior que o tamanho do time
        print(f'ERRO! Não existe o jogador {busca}')
    else:
        print(f'--Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
        print('-'*20)
    print('Fim!!!')

