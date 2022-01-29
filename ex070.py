preco = tot = mil = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont +=1
    tot = tot + preco
    if preco >= 1000:
        mil = mil + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if resp == 'N':
        break
print('-----Fim da comora-----')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mil} produtos custando mais que R$1000')
print(f'O produto mais barato é o {barato} que custa R${menor}')
print('{:=^40}'.format('fim do programa'))