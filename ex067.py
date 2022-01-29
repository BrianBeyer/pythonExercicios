num = c = resp = 0
while True:
    num = int(input('Quer ver a tabuada de qual numero?'))
    if num < 0:
        break
    for c in range(1,11):
        resp = c * num
        print(f'{num} X {c} = {resp}')
print('Fim da tabuada!')
