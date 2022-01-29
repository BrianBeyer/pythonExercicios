nome = str(input('Digite seu nome:')).strip()#strip para eliminar espaço antes e depois
print('Nome em maiusculo:',nome.upper())
print('Nome em minusculo:',nome.lower())
print('Letras ao total sem considerar espaço:', len(nome)-nome.count(' '))#menos os espaços
#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O nome tem {} letras'.format(len(separa[0])))