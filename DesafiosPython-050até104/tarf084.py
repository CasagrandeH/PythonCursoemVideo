lista = []
pesadoNome = None
pesadoPeso = None
leveNome = None
levePeso = None
while True:
    print('-'*120)
    nome = str(input('Nome: ')).capitalize()
    peso = float(input('Peso: '))
    print('-' * 120)
    lista.append([nome, peso])
    if pesadoNome is None or peso > pesadoPeso[0]:
        pesadoNome = [nome]
        pesadoPeso = [peso]
    elif peso == pesadoPeso[0]:
        pesadoNome.append([nome])
    if leveNome is None or peso < levePeso[0]:
        leveNome = [nome]
        levePeso = [peso]
    elif peso == levePeso[0]:
        leveNome.append([nome])
    rep = str(input('Repetir? ( S / N ): ')).strip()
    if rep in 'Nn':
        break
print('-'*120)
print(f'Os cadastros foram: {lista}')
print('-'*120)
print(f'{len(lista)} pessoas foram cadastradas.')
print('-'*120)
if len(pesadoNome) == 1:
    print(f'A pessoa mais pesada foi {pesadoNome[0]}, pesando {pesadoPeso[0]}kgs.')
    print('-' * 120)
else:
    print(f'O maior peso registrado foi de {pesadoPeso[0]}kgs por {pesadoNome[0:1][0]},', end= '')
    for nome in pesadoNome[1:][0]:
        print(f' {nome}', end=', ')
    print('e só.')
    print('-' * 120)
if len(leveNome) == 1:
    print(f'A pessoa mais leve foi {leveNome[0]}, pesando {levePeso[0]}kgs.')
    print('-' * 120)
else:
    print(f'O peso mais leve registrado foi de {levePeso[0]}kgs por {leveNome[0:1][0]},', end= '')
    for nome in leveNome[1:][0]:
        print(f' {nome}', end=', ')
    print('e só.')
    print('-' * 120)
print()
print('END.')