from math import factorial
n = int(input('Digite um numero para saber o fatorial:'))
#print(factorial(n))
c = n
f = 1
print('Calculando {}! = '.format(n),end=' ')
while c > 0:
    print('{}'.format(c),end=' ')
    print('X' if c>1 else ' = ', end=' ')
    f *= c # é igual f=f*c
    c -= 1
print(f)
