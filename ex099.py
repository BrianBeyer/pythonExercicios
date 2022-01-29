from time import sleep


def maior(* m):
    cont = maior = 0
    print('=-'*30)
    print('Analisando os valores...')
    for valor in m:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'foram informados {cont} valores ao todo.')
    print('O maior valor informado foi ',maior)


maior(1, 2, 3, 44, 5, 6, 7, 4, 1)
maior(5, 6, 2, 9)
maior(1, 2)