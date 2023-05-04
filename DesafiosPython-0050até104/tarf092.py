from datetime import date
ano = date.today().year
ficha = dict()
ficha['nome'] = str(input('Qual seu nome?: ')).capitalize()
anoNas = int(input('Qual seu ano de nascimento?: '))
ficha['idade'] = ano - anoNas
ficha['ctps'] = int(input('Qual sua carteira de trabalho? ( 0 irá pular): '))
if ficha['ctps'] == 0:
    print(ficha)
    print(f'O nome é {ficha["nome"]}.')
    print(f'A idade é {ficha["idade"]}.')
    print(f'A carteira de trabalho é nula.')
else:
    ficha['contratação'] = int(input('Em que ano foi contratado?: '))
    ficha['aposentaria'] =  35 - (ano - ficha['contratação'])
    ficha['salario'] = float(input('Qual seu salario?: '))
    print(ficha)
    print(f'O nome é {ficha["nome"]}.')
    print(f'A idade é {ficha["idade"]}.')
    print(f'A carteira de trabalho é {ficha["ctps"]}.')
    print(f'O ano de contratação foi {ficha["contratação"]}.')
    print(f'O salario é R${ficha["salario"]}')
    if ficha['aposentaria'] <= 0:
        print('Ja pode se aposentar.')
    else:
        print(f'{ficha["aposentaria"]} anos até se aposentar.')
print('\nEND.')