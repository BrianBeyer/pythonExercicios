n = str(input('Digite seu nome completo:')).lower().strip()
nome = n.split()
print('Seu primeiro nome é:',nome[0])
print('Seu ultimo nome é:{} '.format(nome[len(nome)-1]))# para mostrar o ultimo nome