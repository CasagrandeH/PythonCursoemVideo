from random import choice
from time import sleep
print('\033[1;97;45m Jokenpô semi-automatico!!! \033[m')
sleep(1)
x = 'PEDRA'
y = 'PAPEL'
z = 'TESOURA'
a = 'PEDRA'
b = 'PAPEL'
c = 'TESOURA'
lista = [x, y, z]
com = choice(lista)
play = str(input('{}{}{}\n{}{}{}\n{}{}{}'.format('\033[0;30;107m','a = PEDRA', '\033[m', '\033[0;30;107m', 'b = PAPEL', '\033[m', '\033[0;30;107m', 'c = TESOURA', '\033[m')))
if play.lower() == 'a':
    play = a
elif play.lower() == 'b':
    play = b
elif play.lower() == 'c':
    play = c
sleep(1)
print('\033[0;31;107mJO\033[m',end= '')
sleep(1)
print('\033[0;34;107mKEN\033[m',end= '')
sleep(1)
print('\033[0;33;107mPÔ!\033[m')
sleep(0.75)
if com == x and play == b or com == y and play == c or com == z and play == a:
    print('\033[0;30;107m PARABÉNS! O jogador ganhou. \033[m')
elif com == x and play == c or com == y and play == a or com == z and play == b:
    print('\033[0;30;107m PERDESTE! O computador te mamou. \033[m')
elif com == play:
    print('\033[0;30;107m EMPATE! Ambos jogaram a mesma parada. \033[m')
print('\033[0;30;107m O computador jogou {}, e o player {}. \033[m'.format(com, play))
