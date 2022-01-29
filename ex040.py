print('+=-'*20)
print('Abaixo de 5 reprovado\nEntre 5 e 6.9 recuperação\n7 ou acima aprovado')
print('+=-'*20)
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if media<5:
    print('Reprovado! Sua nota foi {}'.format(media))
elif media>=5 and media<7:
    print('Recuperação! Sua nota foi {}'.format(media))
elif media>=7:
    print('Aprovado! Sua nota foi {}'.format(media))
