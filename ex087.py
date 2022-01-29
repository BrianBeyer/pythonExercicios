matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')

'''lista = []
v1 = []
v2 = []
v3 = []
soma1 = soma2 = soma3 = 0
for c in range(0,3):
    n1 = int(input(f'Digite um valor para [0, {c}]: '))
    v1.append(n1)
    if n1%2==0:
        soma1 = soma1 + n1
lista.append(v1)
for d in range(0,3):
    n2 = int(input(f'Digite um valor para [1, {d}]: '))
    v2.append(n2)
    if n2%2==0:
        soma2 = soma2 + n2
lista.append(v2)
for e in range(0,3):
    n3 = int(input(f'Digite um valor para [2, {e}]: '))
    v3.append(n3)
    if n3%2==0:
        soma3 = soma3 + n3
lista.append(v3)
print('=-'*20)
print('[',lista[0][0],'][',lista[0][1],'][',lista[0][2],']')
print('[',lista[1][0],'][',lista[1][1],'][',lista[1][2],']')
print('[',lista[2][0],'][',lista[2][1],'][',lista[2][2],']')
print('=-'*20)
print(f'A soma de todos os valores pares é: {soma1+soma2+soma3}' )
print(f'A soma dos valores da terceira coluna é: {n1+n2+n3}')
print(f'O maior valor da segunda linha é: {max(v2)}')'''