Ficha = []
Notas = []
while True:
    Nome = str(input('Nome do Aluno: ')).capitalize()
    NotaUm = float(input('1ª Nota: '))
    NotaDois = float(input('2ª Nota: '))
    Alunos = [Nome, [NotaUm, NotaDois]]
    if Alunos[1] in Notas:
        Notas[Notas.index(Alunos[1])].append(Alunos[0])
    else:
        Notas.append(Alunos[1])
        Ficha.append(Alunos)
        rep = str(input('Continuar? [S/N]: ')).strip().upper()[0]
        if rep in 'Nn':
            break
print('-='*35)
print(f'{"Nº.":<4}{"Nome":<10}{"Média":>8}')
for pos, num in enumerate(Ficha):
    print(f'{pos:<4}{Ficha[pos][0]:<10}{(sum(Ficha[pos][1]))/2:>8.2f}')
while True:
    print('-='*35)
    rep = str(input('Verificar as notas de algum aluno especifico? [S/N]: ')).strip().upper()[0]
    if rep in 'Nn':
        print('-=' * 35)
        break
    Al = int(input('Verificar a nota do aluno: '))
    print(f'As notas de {Ficha[Al][0]} foram: {Ficha[Al][1]}')
    rep = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if rep in 'Nn':
        print('-=' * 35)
        break
print('\nEND.')
