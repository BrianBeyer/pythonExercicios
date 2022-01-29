listanum =[]
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c ==0:#para o primeiro valor a ser lido
        mai = men = listanum[c]#o maior tambem é o menor
    else:
        if listanum[c] > mai:#se o valor da lista for maior que mai ai o valor passa a ser ele
            mai = listanum[c]
            if listanum[c] < men:#se o valor da lista for menor que o menor valor ai men passa a ser ele
                men = listanum[c]
print(f'OS valores digitados foram {listanum}')
print(f'O maior valor foi {mai} na posição ',end='')
for i,v in enumerate(listanum):
    if v == mai: #se o v for o maior
        print(f'{i}...',end='')
print()
print(f'O menor valor foi {men} na posição ',end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
