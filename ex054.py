from datetime import date
d = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    n = int(input('Digite o ano de nascimento da {}° pessoa:'.format(c)))
    if (d-n)>=21:
        maior +=1
    else:
        menor +=1

print('{} pessoas atingiram a maioridade.'.format(maior))
print('{} pessoas são menores de idade.'.format(menor))