galera = []
pessoa = {}
soma = 0
media = 0
while True:
    pessoa.clear()#para limpar e receber uma nova pessoa
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]#0 para pegar so a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']# para somar a idade das pessoas
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N!')
    if resp == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')# mostrar o tamanho da lista
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos.')#5 casas ao total com 2 decimais
print(f'As mulheres cadastradas foram:',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()
print('Lista das pessoas com idade acima da media:',end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<>ENCERRANDO<>')

