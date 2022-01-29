num = cont = soma = 0
while True:
    num = int(input('Digite um numero. [999 para sair!]:'))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'A soma dos {cont} valores foi {soma}!')