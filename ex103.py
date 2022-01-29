def ficha(jog='<Desconhecido!>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':# se tidado todos os espaços ele ficar vazio
    ficha(gol=g)
else:
    ficha(n, g)
