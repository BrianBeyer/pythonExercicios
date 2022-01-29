n = (int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 aparece na {n.index(3)+1}° posição')
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares digitados foram')
for par in n:
   if par%2==0:
       print(par,'-',end=' ')
