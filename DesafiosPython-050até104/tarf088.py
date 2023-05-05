from time import sleep
from random import randint
print('-='*27)
print(f'{"MEGA SENA":^50}')
print('-='*27)
Vezes = int(input('Quantos palpites da MEGA gerar?: '))
print('-='*27)
print(f'{"SORTEANDO":.^25}{Vezes:.^2}{"VEZES":.^25}')
for c in range(0, Vezes):
    Palpite = []
    while len(Palpite) < 6:
        Num = randint(1,60)
        if Num not in Palpite:
            Palpite.append(Num)
    Palpite.sort()
    print(f'{"Palpite":^15}', end= ' ')
    print(f'{c+1:<5}:', end= ' ')
    print(f'{Palpite}')
    sleep(0.5)
print(f'{"BOA SORTE!":.^52}')
print('-='*27)
