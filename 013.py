s = float(input('Qual o salario do funcionario? R$'))
ns = s+(s*15/100)
print('O salario de R${:.2f} com aumento de 15% fica R$ {}' .format(s,ns))