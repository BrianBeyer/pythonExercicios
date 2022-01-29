print('-=-=-=-=-=-Emprestimo bancario-=-=-=-=-=')
casa = float(input('Qual o valor do imovel? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos você vai pagar?'))
prestacao = casa/(anos*12)
sal = salario*30/100
if prestacao>=sal:
    print('A prestação é maior que 30% do seu salario, emprestimo negado!')
else:
    print('Emprestimo aprovado, a prestação em {} anos é R${:.2f}.'.format(anos,prestacao))
