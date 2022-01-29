v = float(input('Qual a distancia da viagem? Km: '))
v1 = v*0.5
v2 = v*0.25
if v<=200:
    print('O preço da passagem é R${:.2f}'.format(v1))
else:
    print('O preço da passagem é R${:.2f}'.format(v2))


