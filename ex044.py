print('{:=^40}'.format('Lojas Guanabara'))#40 caracteres
prod = float(input('Digite o preço do produto: R$'))
print('''Forma de pagamento
[1] à vista dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Digite sua opção:'))

vista = prod-(prod*10/100)
card5 = prod-(prod*5/100)
card3x = prod+(prod*20/100)
if op==1:
    print('À vista no dinheiro ou cheque: R${}'.format(vista))
elif op==2:
    print('À vista no cartão com 5% de desconto: R${}'.format(card5))
elif op==3:
    print('Em até 2x no cartão: R${}, R${}por mes'.format(prod,prod/2))
elif op==4:
    totparc = int(input('Quantas parcelas?'))
    parcela = card3x/totparc
    print('Sua compra sera parcelada em {}x de R${:.2f}, total de R${}'.format(totparc,parcela,card3x))
else:
    print('Opção invalida')



