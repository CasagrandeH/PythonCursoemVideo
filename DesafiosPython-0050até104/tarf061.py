num = int(input('NUMERO:'))
razao = int(input('RAZAO:'))
count = 0
while count != 10:
    print('[ {} ] '.format(num), end= '')
    num += razao
    count += 1
