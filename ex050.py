r = 0
for c in range(1,7):
    par = int(input('Digite um numero:'))
    if par%2==0:
        r += par
print('A soma dos numeros pares é: {}'.format(r))