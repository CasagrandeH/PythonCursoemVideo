from random import randint
vitorias_consecutivas = par = impar = 0
lista = (0,1,2,3,4,5,6,7,8,9,10)
while True:
    jogar = 'S'
    com = randint(0, 10)
    choice = input('Par ou Impar?: ').strip().upper()[0]
    while choice not in ['P', 'I']:
        choice = input('Resposta invalida. Par ou Impar?: ').strip().upper()[0]
    player = int(input('Qual seu numero de [ 0 ] a [ 10] ?: '))
    while player not in lista:
        player = int(input('Numero invalido. Qual seu numero de [ 0 ] a [ 10 ]?: '))
    if choice == 'P':
        total = com + player
        par += 1
        if total % 2 == 0:
            print('O jogador venceu! Parabens!')
            print(f'O jogador jogou [ {player} ], o computador [ {com} ]\nTotalizando [ {total} ]')
            vitorias_consecutivas += 1
        else:
            print('O computador venceu! Mais sorte na proxima!')
            print(f'O jogador jogou [ {player} ], o computador [ {com} ]\nTotalizando [ {total} ]')
            vitorias_consecutivas = 0
    else:
        total = com + player
        impar += 1
        if total % 2 == 0:
            print('O computador venceu! Mais sorte na proxima!')
            print(f'O jogador jogou [ {player} ], o computador [ {com} ]\nTotalizando [ {total} ]')
            vitorias_consecutivas = 0
        else:
            print('O jogador venceu! Parabens!')
            print(f'O jogador jogou [ {player} ], o computador [ {com} ]\nTotalizando [ {total} ]')
            vitorias_consecutivas += 1
    jogar = input('Jogar de novo? ( Sim / Não ): ').strip().upper()[0]
    while jogar not in ['S','N']:
        jogar = input('Jogar de novo? ( Sim / Não ): ').strip().upper()[0]
    if jogar == 'N':
        break
print(f'''O jogador teve [ {vitorias_consecutivas} ] vitorias consecutivas.
O jogador jogou par [ {par} ] vezes, e impar [ {impar} ] vezes.''')