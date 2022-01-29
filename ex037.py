num = int(input('Digite um numero:'))
print('''Escolha uma opção:
 [1] converter para Binario
 [2] converter para Octal
 [3] converter para Hexadecimal''')
op = int(input('Sua opção:'))
if op==1:
    print('{} convertido para Binario: {}'.format(num,bin(num)[2:]))
elif op==2:
    print('{} convertido para Octal: {}'.format(num,oct(num)[2:]))
elif op==3:
    print('{} convertido para Hexadecimal {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida!')