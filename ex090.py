aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f"Média de {aluno['Nome']}: "))
if aluno['Media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
     print(f'{k} é igual a {v}')
