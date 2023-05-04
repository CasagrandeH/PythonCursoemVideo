s = 0
for n in range(0 ,6):
    n = int(input('DIGITE UM NUMERO INTEIRO:'))
    if n % 2 == 0:
        s = s + n
if s != 0:
    print('A soma dos pares é {}.'.format(s))
else:
    print('Não há pares.')
print('FIM.')
