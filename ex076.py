lista = ('Pão',14,'Bolacha',3.5,'Mel',4,'Goiaba',4.5,'Kaki',5)
print('-'*40)
print(f'{"Lista de compras":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos%2 ==0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:7.2f}')#alinhamento a esquerda com 2 casas decimais
print('-' * 40)