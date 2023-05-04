print('-='*30)
print('CONFIRA A TABUADA DE UM NUMERO DE SUA ESCOLHA!')
print('-='*30)
n = int(input('DIGITE UM NUMERO:'))
print('-='*30)
for c in range(0 , 11):
    t = n * c
    print('{} x {} = {}'.format(n, c, t))
print('-='*30)

