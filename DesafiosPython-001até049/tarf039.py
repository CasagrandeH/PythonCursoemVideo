ano = int(input('INFORME A SUA IDADE:'))
if ano < 18:
    ano_t = 18 - ano
    if ano_t == 1:
        print('Em {} ano terás idade suficiente para se alistar no exército, marinha, ou aéronautica.'.format(ano_t))
    else:
        print('Em {} anos terás idade suficiente para se alistar no exército, marinha, ou aéronautica.'.format(ano_t))
elif ano > 18:
    ano_t = ano - 18
    if ano_t == 1:
        print('Se ainda não se alistou estás {} ano atrasado.'.format(ano_t))
    else:
        print('Se ainda não se alistou estás {} anos atrasado.'.format(ano_t))
elif ano == 18:
    print('Chegou a hora de se alistar.')
