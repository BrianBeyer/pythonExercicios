pt = int(input('Primeiro termo:'))
r = int(input('Razão:'))
print('*'*6,'Gerador de Progressão aritimetica','*'*6)
cont = 1
while cont <10:
    print(pt,'>',end=" ")
    pt = pt+r
    cont +=1
print('Fim')
