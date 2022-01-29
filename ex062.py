pt = int(input('Primeiro termo:'))
r = int(input('Razão:'))
print('*'*6,'Gerador de Progressão aritimetica','*'*6)
cont = 1
total = 0
nt = 10
while nt !=0:
    total += nt
    while cont <= total:
        print(pt,'>',end=" ")
        pt = pt+r
        cont +=1
    nt = int(input('\nQuantos termos que mostrar a mais? '))
print('Finalizado com {} termos.'.format(total))
