num = 0
cont = 0
soma = 0
num = int(input('Digite um valor [999 para]:'))
while num != 999:
    cont = cont + 1
    soma += num
    num = int(input('Digite um valor [999 para]:'))
print('Foram digirados {} numeros e sua soma é {}'.format(cont,soma))