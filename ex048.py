soma = 0
cont = 0
for n in range(1,500+1,2):
     if n%3==0:
        cont = cont + 1
        soma += n
print('A soma dos {} numeros impares multipos de 3 é {}'.format(cont,soma))
