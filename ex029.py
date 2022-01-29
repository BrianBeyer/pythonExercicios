km = float(input('Qual a velocidade do carro? Km/h: '))
mm = (km-80)*7
if km>80:
    print('Multado! A velocidade foi {}Km/h e a mulda é de R${:.2f}.'.format(km,mm))
else:
    print('Tenha um bom dia!')