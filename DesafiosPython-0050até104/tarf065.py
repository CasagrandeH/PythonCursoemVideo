from time import sleep
count = 1
media = num = choice = 0
while choice != 2:
    try:
        num = int(input('\n---VALOR {}---\n'.format(count)))
    except ValueError:
        print('Por favor digite apenas numeros inteiros.')
        continue
    media += num
    count += 1
    choice = int(input('CONTINUAR?\n[ 1 = SIM ]\n[ 2 = NÃO ]'))
    sleep(1)
    if choice <= 0:
        print('INVALIDO TENTE NOVAMENTE.')
        count -= 1
    if choice > 2:
        print('INVALIDO TENTE NOVAMENTE.')
        count -= 1
print('A média desses {} numeros é {}.'.format(count - 1, media / (count - 1)))