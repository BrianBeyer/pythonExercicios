from datetime import datetime

lista = []
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input('Anos de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['CPTS'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if pessoa['CPTS'] > 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salario: R$ '))
    pessoa['Aposentadoria'] = pessoa['idade'] + ((pessoa['Ano de contratação'] + 35) - datetime.now().year)
print('-'*30)
for k, v in pessoa.items():
    print(f'O {k} tem o valor {v}')