valores =[]
for cont in range(0,5):
    n = (int(input(f'Digite o {cont+1}° valor:')))
    if cont == 0 or n > valores[-1]:#sese o n for maior que o numero que estiver no ultimo elemento (-1) :
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print(f'Os valores digitados em ordem foram {valores}')
