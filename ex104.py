def leiaint(msg):
    ok = False
    valor=0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print("\033[0;31mErro! Digite um numero inteiro.\033[m")
        if ok:
           break
    return valor

n = leiaint('Digite um numero: ')
print(f'Voceê digitou o numero {n}')