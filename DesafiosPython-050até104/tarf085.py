ListaTotal = []
Par = []
Impar = []
for c in range(1,8):
    Numero = int(input(f'Digite o {c}º numero: '))
    if Numero % 2 == 0:
        Par.append(Numero)
    elif Numero % 2 != 0:
        Impar.append(Numero)
Par.sort()
Impar.sort()
ListaTotal.append([Par])
ListaTotal.append([Impar])
print('-='*25)
print(f'Os numeros pares em ordem crescente foram: ', end= '')
for num in ListaTotal[0]:
    print(f'{num}', end= ' ')
print(f'\nOs numeros ímpares em ordem crescente foram: ', end= '')
for num in ListaTotal[1]:
    print(f'{num}', end= ' ')
print('\nEND.')