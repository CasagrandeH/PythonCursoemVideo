def contagem(inicio, fim, passo):
    print(f'A contagem tem o inicio em {inicio}, termina em {fim}, e vai de {passo} em {passo}. \nEX: ', end= '')
    if passo == 0:
        if passo < 0:
            for c in range(inicio, fim - 1, passo - 1):
                print(f'{c}', end=' ', flush= True)
                sleep(0.4)
            print('Fim.')
        else:
            for c in range(inicio, fim + 1, passo + 1):
                print(f'{c}', end=' ', flush= True)
                sleep(0.4)
            print('Fim.')
    else:
        if passo < 0:
            for c in range(inicio, fim - 1, passo):
                print(f'{c}', end=' ', flush= True)
                sleep(0.4)
            print('Fim.')
        else:
            for c in range(inicio, fim + 1, passo):
                print(f'{c}', end= ' ', flush= True)
                sleep(0.4)
            print('Fim.')


#programa principal
from time import sleep
contagem(1,10,1)
contagem(10,0,-2)
print('-='*30)
contagem(inicio= int(input('Passo: ')), fim= int(input('Fim: ')), passo= int(input('Passo: ')))
print('-='*30)