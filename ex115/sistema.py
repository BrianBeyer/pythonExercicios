from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if arquivoexiste(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo nao encontrado')
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        # opçoao de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # cadastrar nova pessoa
        cabecalho('Novo cadastro ')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo...')
        break
    else:
        print('\033[31mERRO!!!\033[m')