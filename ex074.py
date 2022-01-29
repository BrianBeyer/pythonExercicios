import random
al = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print('OS valores sorteados foram')
for n in al:
    print(f'{n} ',end=' ')
print(f'\nO maior foi {max(al)}')
print(f'O menor foi {min(al)}')