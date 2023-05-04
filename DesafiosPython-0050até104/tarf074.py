from random import randint
while True:
    tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
    print(f'A tupla gerada foi: \n{tupla}')
    print(f'O maior numero foi: \n[ {max(tupla)} ]')
    print(f'O menor numero foi :\n[ {min(tupla)} ]')
    print('-='*15)
    choice = input('(S/N)').strip().upper()
    print('-='*15)
    if choice == 'N':
        break
print('END.')