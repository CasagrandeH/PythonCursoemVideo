num = int(input('PRIMEIRO TERMO:'))
num1 = num
razao = int(input('RAZÃO:'))
count = 0
choice = 0
while count != 10:
    print('[{:^10}] '.format(num1), end= '')
    num1 += razao
    count += 1
while choice != 2:
    print('\n', '-=' * 30)
    choice = int(input('[ 1 ] MOSTRAR MAIS TERMOS\n[ 2 ] NÃO MOSTRAR MAIS TERMOS'))
    print('-='*30)
    if choice < 1:
        print('ERRO!')
    if choice > 2:
        print('ERRO!')
    else:
        termos = int(input('QUANTOS TERMOS?:'))
        count = 0
        num1 = num
        while count != termos:
            print('[{:^10}] '.format(num1), end= '')
            num1 += razao
            count += 1
            if count % 10 == 0:
                print('\n', end= '')
print('FIM.')