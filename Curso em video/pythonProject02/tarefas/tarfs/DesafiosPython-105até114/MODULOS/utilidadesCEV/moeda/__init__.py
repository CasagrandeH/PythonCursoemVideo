def aumentar(a=0, por=0, format=False):
    aum = a + (a * (por/100))
    if format is True:
        real = f'R${aum:.2f}'
        return real
    else:
        return aum


def diminuir(a=0, por=0, format=False):
    dim = a - (a * (por/100))
    if format is True:
        real = f'R${dim:.2f}'
        return real
    else:
        return dim


def dobro(a=0, format=False):
    dob = a * 2
    if format is True:
        real = f'R${dob:.2f}'
        return real
    else:
        return dob


def metade(a=0, format=False):
    met = a / 2
    if format is True:
        real = f'R${met:.2f}'
        return real
    else:
        return met

def moeda(a=0):
    real = f'R${a:.2f}'
    return real

def titulo(msg):
    tam = len(msg) + 16
    print('-'*tam)
    print(f'        {msg}')
    print('-'*tam)


def resumo(num=0, aum=0, dim=0, dob=False, met=False):
    titulo('TABELA DE RESUMO')
    if aum != 0:
        aumento = num + (num * (aum / 100))
        print(f'{aum}% de juros:{"":<7}R${aumento:.2f}')
    if dim != 0:
        diminui = num - (num * (dim / 100))
        print(f'{dim}% de desconto:{"":<4}R${diminui:.2f}')
    if dob is not False:
        dobr = num * 2
        print(f'{"DOBRO:":<12}{"":<8}R${dobr:.2f}')
    if met is not False:
        metad = num / 2
        print(f'{"METADE:":<12}{"":<8}R${metad:.2f}')
