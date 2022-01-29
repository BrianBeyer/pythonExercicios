print('+'*20)
print('Calculando IMC')
print('+'*20)
peso = float(input('Qual seu peso?(Kg)'))
alt = float(input('Qual sua altura?(m)'))
imc = peso/(alt**2)
if imc<18.5:
    print('IMC {:.2f}, abaixo do peso'.format(imc))
elif 18.5 <= imc <25:#outra forma de escrever
    print('IMC {:.2f}, peso ideal'.format(imc))
elif imc>=25 and imc<30:
    print('IMC {:.2f}, sobrepeso'.format(imc))
elif imc>=30 and imc<40:
    print('IMC {:.2f}, obesidade'.format(imc))
elif imc>40:
    print('IMC {:.2f}, obesidade mórbida'.format(imc))
