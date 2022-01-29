s = str(input('Digite o sexo: [M/F]:')).upper().strip()[0]#0 para pegar so a primeira letra
while s not in 'MF':
    s = str(input('Dados invalidos, digite novamente o sexo: ')).upper().strip()
print('O sexo é {}'.format(s))


