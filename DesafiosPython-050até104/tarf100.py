def sorteado(a):
    num = ()
    for c in range(0, a):
        num += (randint(1,100),)
    return num


def somaPar(num):
    pares = ()
    for c in num:
        if c % 2 == 0:
            pares += (c,)
    print(f'Os valores sorteados foram: {num}')
    print(f'Os valores pares foram {pares}. E sua soma é {sum(pares)}.')


from random import randint
numeros = sorteado(5)
somaPar(numeros)
numeros = sorteado(5)
somaPar(numeros)