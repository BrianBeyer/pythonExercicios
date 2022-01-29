maior = mulher20 = homem = 0
homem = 0

print('---CADASTRO DE PESSOAS---')
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        maior = maior + 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 = mulher20 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de {maior} pessoas com mais de 18 anos.')
print(f'Ao total foram {homem} homens cadastrados')
print(f'Temos {mulher20} mulheres com menos de 20 anos.')