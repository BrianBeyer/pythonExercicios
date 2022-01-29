matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

'''lista = []
v1 = []
v2 = []
v3 = []
for c in range(0,3):
    #v1.append(int(input(f'Digite um valor para [0, {c}]: ')))
lista.append(v1)
for d in range(0,3):
    #v2.append(int(input(f'Digite um valor para [1, {d}]: ')))
lista.append(v2)
for e in range(0,3):
    #v3.append(int(input(f'Digite um valor para [2, {e}]: ')))
lista.append(v3)
print('=-'*20)
print('[',lista[0][0],'][',lista[0][1],'][',lista[0][2],']')
print('[',lista[1][0],'][',lista[1][1],'][',lista[1][2],']')
print('[',lista[2][0],'][',lista[2][1],'][',lista[2][2],']')
'''