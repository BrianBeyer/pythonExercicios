somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1,5):
    print('----{}° pessoa ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p== 1 and sexo in 'Mm':#in m e M procura em m maiusculo ou minusculo
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
            totmulher20 +=1
mediaidade = somaidade / 4
print('A media da idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))