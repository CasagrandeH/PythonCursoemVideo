lista = []
listaPar = []
listaImpar = []
while True:
    valor = str(input('DIGITE UM NUMERO: '))
    while not valor.isnumeric():
        valor = input('INVALIDO! DIGITE UM NUMERO: ')
    valor = int(valor)
    lista.append(valor)
    continuar = input('Continuar? ( S / N ): ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Tente novamente. Continuar? ( S / N ): ').strip().upper()[0]
    if continuar == 'N':
        break
for num in lista:
    if num % 2 == 0 and num not in listaPar:
        listaPar.append(num)
    elif num % 2 != 0 and num not in listaImpar:
        listaImpar.append(num)
listaPar.sort()
listaImpar.sort()
print(f'A lista gerada foi: {lista}.')
print(f'Os numeros pares da lista foram: {listaPar}.')
print(f'Os numeros impares da lista foram: {listaImpar}.')
