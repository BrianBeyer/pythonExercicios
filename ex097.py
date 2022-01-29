def escreva(txt):
    x = len(txt)+4
    print('~'*x)
    print(f'  {txt}')
    print('~'*x)


txt = str(input('Digite o texto: '))
escreva(txt)
