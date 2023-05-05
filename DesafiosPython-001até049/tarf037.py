sel = int(input('1 = BINARIO \n2 = OCTAL \n3 = HEXADECIMAL'))
if sel == 1:
    b = int(input('VALOR PARA CONVERTER PARA BINARIO:'))
    print('{} ='.format(b), bin(b)[2:])
elif sel == 2:
    o = int(input('VALOR PARA CONVERTER PARA OCTAL:'))
    print('{} ='.format(o), oct(o)[2:])
elif sel == 3:
    h = int(input('VALOR PARA CONVERTER PARA HEXADECIMAL:'))
    print('{} ='.format(h), hex(h)[2:])
else:
    print('RESPOSTA INVALIDA')

