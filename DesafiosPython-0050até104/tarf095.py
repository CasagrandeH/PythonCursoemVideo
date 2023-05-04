Lista = []
while True:
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
    Lista.append(Jogador.copy())
    Jogador.clear()
    gols.clear()
    rep = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if rep in 'N':
        break
print('-='*15)
print(f'{"Cdg.":<2}{"Nome":<12}{"Gols"}{"TOTAL":>20}')
for c in range(0, len(Lista)):
     print(f'{c:<2} {Lista[c]["nome"]:<12} {Lista[c]["gols"]} {Lista[c]["campeonato"]:^20}')
print('-=' * 15)
rep = str(input('Quer puxar informação de um jogador especifico? [S/N]: ')).strip().upper()[0]
print('-='*15)
if rep not in 'N':
    while True:
        visual = int(input('Codigo do jogador (999 Cancela): '))
        if visual in 999:
            break
        else:
            print(f'=-=-LEVANTAMENTO DO JOGADOR {Lista[visual]["nome"]}-=-=')
            for c in range(0, len(Lista[visual]['gols'])):
                print(f'Na {c+1}ª partida marcou {Lista[visual]["gols"][c]} gols')
else:
    print('\nFIM.')