def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Digite um numero inteiro.\033[m")
            continue  # joga para o laço de novo a partir daqui
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
           n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Digite um numero real.\033[m")
            continue  # joga para o laço de novo a partir daqui
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n


n1 = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')