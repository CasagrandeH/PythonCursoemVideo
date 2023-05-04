lista = []
for c in range(0,5):
    lista.append(int(input(f'DIGITE UM VALOR PARA A POSIÇÃO {c}: ')))
print(f'A lista gerada foi {lista}.')
print(f'O maior numero foi {max(lista)} na posição', end= ' ')
for pos, count in enumerate(lista):
    if count == max(lista):
        print(f'{pos}...', end= ' ')
print(f'\nO menor valor foi {min(lista)} na posição', end=' ')
for pos, count in enumerate(lista):
    if count == min(lista):
        print(f'{pos}...', end=' ')
print('\nEND.')
