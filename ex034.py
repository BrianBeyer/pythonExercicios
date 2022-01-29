s = float(input('Qual o salario do funcionario: RS:'))
s1 = s+(s*10/100)
s2 = s + (s*15/100)
if s>1250:
    print('O novo salario com aumento de 10% é: {}'.format(s1))
if s<=1250:
    print('O novo salario com aumento de 15% é {}'.format(s2))
