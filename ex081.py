valores = []
c = 0
resp = 'S'
cinco = 0
while resp in 'Ss':
    v = valores.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    c+=1
print(f'Você digitou {c} valores')# ou len(valores)
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 foi encontrado na lista! ')
else:
    print(f'O valor 5 não foi encontrado na lista! ')