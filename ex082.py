lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v%2==0:
        par.append(v)
    elif v%2==1:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
