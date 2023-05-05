'''Tupla = ()
Pares = ()
for Pos in range(1,5):
    Valor = int(input('DIGITE O VALOR: '))
    Tupla += (Valor,)
Contador = Tupla.count(9)
for Numero in Tupla:
    if Numero % 2 == 0:
        Pares += (Numero,)
print(f'A tupla gerada foi: {Tupla}')
if 9 in Tupla:
    print(f'O numero 9 apareceu [{Contador}] vezes na tupla.')
else:
    print('O numero 9 não aparece na tupla.')
if 3 in Tupla:
    print(f'A primeira instância de 3 é na posição {Tupla.index(3)}.')
else:
    print('O numero 3 não aparece na tupla.')
if Pares == ():
    print('Não há numeros pares.')
else:
    print(f'Os numeros pares da tupla são: {Pares}')'''
Count = Pares = 0
Numeros = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')))
for Nove in Numeros:
    if Nove == 9:
        Count += 1
for Par in Numeros:
    if Par % 2 == 0:
        Pares += 1
print('-='*20)
print(f'Você digitou os numeros {" ".join(map(str, Numeros[0:5]))}')
print('-='*20)
print(f'O valor 9 apareceu [ {Count} ] vezes.')
print('-='*20)
print(f'A primeira instância de 3 foi na posição [ {Numeros.index(3)} ]')
print('-='*20)
print(f'Há [ {Pares} ] numeros pares na tupla.')


