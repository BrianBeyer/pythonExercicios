frase = str(input('Digite uma frase para saber se é um palindromo: ')).strip().upper()
palavras = frase.split()# para dividir a frase
junto = ''.join(palavras)#para juntar sem espaços ou por oque estiver entre aspas
inverso = ''
for letra in range(len(junto)-1,-1,-1):
   inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('É um palindromo!')
else:
    print('Não é palindromo!')