from time import sleep
num1 = float(input('NUMERO 1:'))
num2 = float(input('NUMERO 2:'))
choice = 0
sleep(0.5)
while choice != 5:
    print('-='*30)
    choice = int(input('[ 1 ] SOMA\n[ 2 ] MULTIPLICADOR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR DO PROGRAMA'))
    print('-='*30)
    sleep(0.5)
    if choice == 1:
        print('A soma de {} e {} é {}.'.format(num1, num2, num1+num2))
    elif choice == 2:
        print('A multiplicação de {} e {} é {}'.format(num1, num2, num1*num2))
    elif choice == 3:
        if num1 > num2:
            print('{} é o maior'.format(num1))
        else:
            print('{} é o maior.'.format(num2))
    elif choice == 4:
        num1 = float(input('NUMERO 1:'))
        num2 = float(input('NUMERO 2:'))
print('FIM.')