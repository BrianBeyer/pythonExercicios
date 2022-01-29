from datetime import date
print('-'*32)
print('Confederação Nacional de Natação')
print('-'*32)
id = int(input('Ano de nascimento:'))
ano = date.today().year
idade = ano-id
if idade<=9:
    print('{} anos, catedoria mirim'.format(idade))
elif idade<=14:
    print('{} anos, categoria infantil'.format(idade))
elif idade<=19:
    print('{} anos, categoria junior'.format(idade))
elif idade==25:
    print('{} anos, categoria sênior'.format(idade))
else:
    print('{} anos, categoria master'.format(idade))
