def notas(*n, sit=False):#*para receber varios valores
    """
    -> para analisar notas e situaçao do aluno
    :param n: uma ou mais notas do aluno
    :param sit: indica se deve ou nao adicionar a situaçao
    :return: dicionario com carias informaçoes sobre a situaçao da turma
    """
    r = {}#dicionario
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:# se a situaçao for verdadeiro
        if r['media'] > 7:
            r['sutuação'] = 'Boa'
        elif r['media'] >= 5:
            r['situaçao'] = 'Razoavel'
        else:
            r['situaçao'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)