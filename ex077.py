print('*'*30)
print('Vogais das palavras')
print('*'*30)
palavra = ('Amarelo','Papel','Açucar','Suco')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

