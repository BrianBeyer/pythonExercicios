def area(lar, com):
    ar = lar * com
    print(f'A área de um terreno de {lar} x {com} é de {ar}m²')


print('Controle de terrenos')
print('-'*15)
lar = float(input('Largura (m): '))
com = float(input('Comprimento (m): '))
area(lar, com)
