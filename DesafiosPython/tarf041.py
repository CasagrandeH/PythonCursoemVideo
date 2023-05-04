from datetime import date
nas = int(input('QUAL SEU ANO DE NASCIMENTO?'))
ano = date.today().year
idade = ano - nas
if idade <= 9:
    print('categoria MIRIM de natação.')
elif idade <= 14:
    print('categoria INFANTIL de natação.')
elif idade <= 19:
    print('categoria JUNIOR de natação.')
elif idade <= 25:
    print('categoria SÊNIOR de natação.')
else:
    print('categoria MASTER de natação.')
