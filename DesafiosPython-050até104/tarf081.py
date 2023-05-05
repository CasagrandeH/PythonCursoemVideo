lista = []
index = list()
while True:
    lista.append(int(input('DIGITE UM VALOR: ')))
    for pos, num in enumerate(lista):
        if num == 5 and pos not in index:
            index += [pos]
    continuar = input('Continuar? ( S / N ): ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Tente novamente.\nContinuar? ( S / N ): ').strip().upper()[0]
    if continuar in 'N':
        break
lista.sort(reverse = True)
print(f'Foram digitados {len(lista)} numeros.')
print(f'A lista em ordem decrescente fica: {lista}')
if index != list():
    print(f'O numero 5 aparece na lista {len(index)} vezes. Nas posições {index}')
else:
    print('O numero 5 não aparece na lista.')
print('END.')
