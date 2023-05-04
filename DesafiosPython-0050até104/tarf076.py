from locale import setlocale, currency, LC_ALL#IMPORTANTE PRA CONVERTER DINHEIRO PRA REAL
setlocale(LC_ALL, 'pt_BR.utf8')#IMPORTANTE PRA CONVERTER DINHEIRO PRA REAL
Produto = ()
while True:
    print('-' * 100)
    try:
        Nome = str(input('Qual o nome do produto?: ')).capitalize()
        while not Nome.isalpha():
            Nome = str(input('DIGITE APENAS LETRAS!\nQual o nome do produto?: ')).capitalize()
        Valor = str(input('E o preço?: '))
        while not Valor.isnumeric():
            Valor = str(input('DIGITE APENAS NUMEROS!\nE o preço?: '))
        Valor = float(Valor)
        Valor = currency(Valor, grouping=True, symbol= 'R$')#IMPORTANTE PRA CONVERTER DINHEIRO PRA REAL
        print('-'*100)
        Produto  += (Nome, Valor,)
    except ValueError:
        print('ERROR!')
        continue
    Continuar = str(input('Continuar? ( S / N )')).strip().upper()[0]
    while Continuar not in 'SN' and not Continuar.isalpha():
        Continuar = str(input('Input INvalido.\nContinuar? ( S / N )')).strip().upper()[0]
    if Continuar == 'N':
        break
print('-'*100)
print('{:^100}'.format('TABELA DE PRODUTOS'))
print('-'*100)
for Item in range(0, len(Produto)):
    if Item % 2 == 0:
        Pontos = (100 - len(Produto[Item]) - len(Produto[Item + 1]))
        print(f'{Produto[Item]:<}', end= '')
        print(f'{"." * Pontos}', end= '')
    else:
        print(f'{Produto[Item]}')
print('-'*100)
