from datetime import date
ano = date.today().year
nasc = int(input('Digite seu ano de nascimento:'))
idade = (ano-nasc)
if idade == 18:
    print('Você tem {} anos, é hora de se alistar no exercito!'.format(idade))
elif (ano-nasc)<18:
    print('Você tem {} anos, faltam {} anos para o alistamento!'.format(idade,(18-idade)))
else:
    print('Você tem {} anos, passou {} anos do prazo do alistamento!'.format(idade,(idade-18)))

