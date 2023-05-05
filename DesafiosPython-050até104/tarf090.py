ficha = {}
ficha['nome'] = str(input('Nome do aluno: ')).capitalize()
ficha['média'] = float(input('Média do aluno: '))
if ficha['média'] >= 7:
    ficha['situação'] = 'Aprovado'
elif 5 <= ficha['média'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'
for k, v in ficha.items():
    print(f'{k} é igual a [{v}].')