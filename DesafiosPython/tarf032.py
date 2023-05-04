from datetime import date
ano = int(input('Que ano analisar: ||coloque 0 para analisar o ano atual||'))
if ano == 0:
    ano = date.today().year
dec = ano % 100
if dec == 00:
    dec = ano % 1000
    cal = dec / 400
    print(dec)
else:
    cal = dec / 4
if cal % 1 == 0:
    print('O ano de {} é um ano bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
