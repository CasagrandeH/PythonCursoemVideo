def ficha(nome='', gols=''):
    if nome == '' and gols != '':
        print(f'O jogador <desconhecido> marcou {gols} gol/s no campeonato.')
    elif gols == '' and nome != '':
        print(f'O jogador {nome} marcou 0 gol/s no campeonato.')
    elif nome == '' and gols == '':
        print(f'O jogador <desconhecido> marcou 0 gol/s no campeonato.')
    else:
        print(f'O jogador {nome} marcou {gols} gol/s no campeonato.')


print('-'*60)
ficha(nome= str(input('Nome do jogador: ')).strip().capitalize(), gols= str(input('Gol/s no campeonato: ')))
print('-'*60)