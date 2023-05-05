from random import choice , randint
from time import sleep
#num = choice([0,1,2,3,4,5])
num = randint( 0,5 )
esco = int(input('EU QUERO JOGAR UM JOGO, HUMANO. AGORA ME ENTERTANHA COM DUA VIDA EM RISCO. ESTOU PENSANDO EM UM NUMERO DE 0 A 5... QUAL SERIA?'))
print('HMMMMMMMMMM.' , end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
if num == esco:
    print('VOCÊ EXCEDE MINHAS EXPECTATIVAS.')
else:
    print('DESAPONTANTE.')
print('O NUMERO DE FATO ERA: {}'.format(num))
