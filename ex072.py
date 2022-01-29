zero = ('ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ',
        'ONZE', 'DOZE','TREZE','CATORZE', 'QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')
num = int(input('Digite um numero entre 0 e 20: '))
while True:
    if num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    else:
        print(f'Você digitou o numero {zero[num]}')
        break
