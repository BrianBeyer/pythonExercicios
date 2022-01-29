from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1# para transformar em positivo
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim: #se o inifio for menor que o fim
            print(f'{cont} ',end='')
            sleep(0.3)
            cont += passo
        print('Fim!!!')
    else:# se o inicio for maior que o fim
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end='')
            sleep(0.3)
            cont -= passo
        print('Fim!!!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

