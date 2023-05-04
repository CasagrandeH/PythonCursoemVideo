print('COMPARE 2 NUMEROS PARA VER QUAL E O MAIOR')
from time import sleep
sleep(1)
n1 = int(input('DIGITE UM VALOR:'))
n2 = int(input('DIGITE OUTRO:'))
if n1 > n2:
    print('O primeiro valor, {} é MAIOR que o segundo valor, {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor, {} é MAIOR que o segundo valor, {}.'.format(n2, n1))
else:
    print('OS VALORES SÃO IGUAIS, então não existe valor maior.')
