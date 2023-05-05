sexo = ''
sexo = str(input('QUAL SEXO? [ M / F ]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('DADOS INVALIDOS! TENTE NOVAMENTE!\nQUAL SEXO? [ M / F ]')).strip().upper()[0]
print('SEXO {}.'.format(sexo))