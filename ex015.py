d = int(input('Quantos dias alugado?'))
k = float(input('Quantos Km rodados?'))
pag = d*60 + k*0.15
print('O valor a ser pago é R${:.2f}' .format(pag))
