import random

print('Jogo Par ou Impar')
vic = 0
while True:
    vc = int(input('Diga um valor:'))
    pc = random.randint(0, 20)
    tot = vc + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P ou I]:')).strip().upper()[0]
    print(f'Voce jogou {vc} e o computador {pc}. Total de {tot}',end=" ")
    print('Deu PAR' if tot %2 == 0 else 'Deu IMPAR' )
    if tipo == 'P':
        if tot %2 == 0:
            print('Você Venceu')
            vic =+ 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você Venceu')
            v =+1
        else:
            print('Você Perdeu')
            break
print(f'Game over! Você venceu {vic} vezes')