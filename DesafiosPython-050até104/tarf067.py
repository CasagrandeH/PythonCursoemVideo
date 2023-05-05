print('CALCULADOR DE TABUADA.\nUSE NUMEROS NEGATIVOS PARA SAIR DO PROGRAMA.')
print('-='*30)
while True:
    numeral = int(input('DIGITE UM NUMERO: '))
    print('-=' * 30)
    expoente = 0
    if numeral < 0:
        break
    while expoente <= 10:
        print(f'[ {numeral} ] x [ {expoente} ] = [ {numeral * expoente} ]')
        expoente += 1
    print('-='*30)
print('Fim.')