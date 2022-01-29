def fatorial(n, mostrar=False):
    """
    -> Calcula fatorial
    :param n: o numero a ser calculado
    :param mostrar: mostrar ou nao a conta
    :return: o valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if mostrar:
            print(c,end='')
            if c > 1:
                print(f' X ',end='')
            else:
                print(' = ',end='')# se o ultimo numero nao for maior que um, aparecer sinal de igual
        f *= c
    return f

fat = int(input('Escolha um numero: '))
print(fatorial(fat, mostrar=True))
help(fatorial)