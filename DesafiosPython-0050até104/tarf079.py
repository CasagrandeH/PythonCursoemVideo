lista = []
while True:
    try:
        valor = int(input('DIGITE UM VALOR: '))
        if valor not in lista:
            lista.append(valor)
            print('Valor adicionado com sucesso.')
        else:
            print('Valor duplicado! Não será adicionado.')
        continuar = input('Continuar? ( S / N ): ').strip().upper()[0]
        if continuar not in 'SN':
            continuar = input('ERRO!\nContinuar? ( S / N ): ').strip().upper()[0]
        if continuar == 'N':
            break
    except ValueError:
        print('ERRO! TENTE NOVAMENTE!')
        continue
lista.sort()
print(f'Em ordem crescente, os valores adicionados foram: {lista}')
print('END.')
