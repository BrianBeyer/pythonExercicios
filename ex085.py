num = [[],[]]
numero = 0
for c in range(1,8):
    numero = (int(input(f'Digite o {c}° numero: ')))
    if numero%2==0:
        num[0].append(numero)
    else:
        num[1].append(numero)
num.sort()
print('Todos os numeros:', num)
num[0].sort()
print('OS valores pares são: ',num[0])
num[1].sort()
print('OS valores impares são: ',num[1])
