num = int(input('QUAL NUMERO?:'))
if num == 0:
    print('O fatorial de 0 é 1.')
if num < 0:
    print('ERRO! O FATORIAL NÃO ESTA DEFINIDO PARA NUMEROS NEGATIVOS..')
else:
    fator = num
    contagem = 1
    while fator != 1:
        contagem *= fator
        fator = fator - 1
print('O fatorial de {} é {}'.format(num, contagem))
