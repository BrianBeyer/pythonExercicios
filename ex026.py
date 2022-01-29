f = str(input('Digite uma frase:')).strip().upper()
f2 = f.count('A')
print('Sua frase tem {} letras A'.format(f2))

print('A letra A, aparece a primeira vez na posição:',f.find('A')+1)

print('A ultima letra A aparece na posição:{}'.format(f.rfind('A')+1)) # para procurar a letra da direita para a esquerda
