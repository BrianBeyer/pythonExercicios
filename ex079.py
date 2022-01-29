numeros = []
while True:
    n =int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Adicionado')
    else:
        print('Valor duplicado! Não adicionado')
    r = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if r in 'Nn':
        break
numeros.sort()
print('Os valores foram:',numeros)