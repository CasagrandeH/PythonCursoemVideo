from time import sleep
from random import randint
from operator import itemgetter
Jogo = {}
Ranking = list()
mai = 0
print('-='*20)
print('-'*40)
print(f'{"VALORES SORTEADOS":^40}')
print('-'*40)
for c in range(1,5):
    Jogo[f'jogador{c}'] = randint(1,6)
    print(f'    O jogador {c} tirou: {Jogo[f"jogador{c}"]}')
    sleep(0.5)
Ranking = sorted(Jogo.items(), key= itemgetter(1), reverse= True)
print('-'*40)
print(f'{"COLOCAÇÃO":^40}')
print('-'*40)
for i, v in enumerate(Ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('-='*20)