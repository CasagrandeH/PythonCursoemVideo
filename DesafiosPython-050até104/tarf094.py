from operator import itemgetter
Lista = []
Ficha = {}
while True:
    Ficha['nome'] = str(input('Nome: ')).capitalize()
    Ficha['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
    Ficha['idade'] = int(input('Idade: '))
    Lista.append(Ficha.copy())
    Ficha.clear()
    rep = str(input('Continuar? (S/N): ')).strip().upper()[0]
    if rep in 'N':
        break
media = sum(map(itemgetter('idade'), Lista)) / len(Lista)#JEITO DE CALCULAR A MEDIA
print('-='*30)
print(f'{len(Lista)} pessoas foram cadastradas.'
      f'\nA média de idade dos cadastros é {media:.2f}.'
      f'\nAs mulheres foram:', end= ' ')
for c in range(0, len(Lista)):
    if Lista[c]['sexo'] == 'F':
        print(f'{Lista[c]["nome"]}...', end= ' ')
print(f'\nAs pessoas com idade acima da media foram:')
for c in range(0, len(Lista)):
    if Lista[c]['idade'] > media:
        print(f'-=-=-= {Lista[c]["nome"]} com {Lista[c]["idade"]} anos e sexo {Lista[c]["sexo"]}.')
print('-='*30)
print('\nEND.')
