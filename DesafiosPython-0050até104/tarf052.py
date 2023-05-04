print('-=' * 30 + '-')
num = int(input('QUAL NUMERO:'))
tot = 0
print('{}RED{} = TRUE \n{}BLUE{} = FALSE'.format('\033[31m', '\033[m', '\033[34m', '\033[m'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[34m', end= '')
    print('{} '.format(c), end= '')
print('\n\033[mO numero {} foi contado {} vezes.'.format(num, tot))
if tot == 2:
    print('Portanto, {} É um numero PRIMO.'.format(num))
else:
    print('Portanto, {} NÃO é um numero PRIMO.'.format(num))
print('FIM.')
print('-=' * 30 + '-')
