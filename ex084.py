lista = []
pess = []
men = 0
mai = 0
while True:
    pess.append(str(input('Nome:')))
    pess.append(float(input('Peso:')))
    if len(lista)==0:# se nao cadastrou ninguem ainda
        mai = men = pess[1]#o maior é o mesmo que o menor e igual pess na posicao 1 que é o peso
    else:
        if pess[1] > mai:
            mai = pess[1]
        if pess[1] < men:
            men = pess[1]
    lista.append(pess[:])
    pess.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ',end='')
for p in lista:#para cada p dentro de lista, vai pegar cada lista e jogar em p
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso foi de {men}Kg. peso de ',end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()




