from datetime import date
menor = 0
maior = 0
data = date.today().year
for i in range(1,8):
    ano = int(input('ANO DE NASCIMENTO:'))
    idade = data - ano
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1
print('{} dos 7 candidatos são menores de idade.'.format(menor))
print('{} dos 7 candidatos são maiores de idade.'.format(maior))
print('FIM.')