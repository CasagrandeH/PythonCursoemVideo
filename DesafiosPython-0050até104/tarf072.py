extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
           'vinte')
while True:
    try:
        posição = int(input('Digite um numero de 0 a 20: '))
        while not 0 <= posição <= 20:
            posição = int(input('Input invalido. Tente novamente.\nDigite um numero de 0 a 20: '))
        print(f'O número {posição} em extenso é {"".join(map(str, extenso[posição].capitalize()))}')
        continuar = input('Repetir? ( S / N ): ').strip().upper()[0]
        while continuar not in 'SN':
            continuar = input('Input invalido. Tente novamente\nRepetir? ( S / N ): ').strip().upper()[0]
        if continuar == 'N':
            break
    except ValueError:
        print('ERRO! COMECE DENOVO!')
        continue
print('END.')
