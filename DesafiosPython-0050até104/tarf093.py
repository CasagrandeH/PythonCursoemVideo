Jogador = {}
gols = []
Jogador['nome'] = str(input('Qual o nome do jogador?: ')).capitalize()
Jogador['jogos'] = int(input(f'Quantas partidas {Jogador["nome"]} jogou?: '))
print('Quantos gols marcou na...')
for c in range(0, Jogador['jogos']):
    print('-'*30)
    gols.append(int(input(f'{c+1}ª partida?: ')))
Jogador['gols'] = gols[:]
Jogador['campeonato'] = sum(gols)
print('-'*30)
print(Jogador)
print('-'*30)
print(f'O campo nome é {Jogador["nome"]}.'
      f'\nO campo gols é {Jogador["gols"]}.'
      f'\nO campo campeonato é {Jogador["campeonato"]}.')
print('-'*30)
for c in range(0, len(gols)):
    print(f'-=-= Na {c+1}ª partida marcou: {gols[c]} =-=-')
print(f'Foi um total de {Jogador["campeonato"]} gols.')
print('-'*30)
