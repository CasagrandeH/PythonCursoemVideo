def leiaDenero(num=''):
    while True:
        try:
            num = num.replace(',', '.')
            num = float(num)
            break
        except ValueError:
            num = input(f'\033[31mERRO! \"{num}\" é um preço inválido!\033[m\nDigite um valor: R$')
    return num


def leiaInt(num):
    while True:
        try:
            num = int(num)
            break
        except (ValueError, TypeError):
            num = input('\033[0;31mValor invalido! Digite um numero inteiro valido!\033[m\nDigite um numero: ')
        except KeyboardInterrupt:
            num = 0
            print(f'\033[0;31mO usuario decidiu deixar o espaço dos numeros INTEIROS vazio.\033[m')
            break
    return num

def leaiFloat(num):
    while True:
        try:
            num = float(num)
            break
        except (ValueError, TypeError):
            num = input(f'\033[0;31mValor invalido! Digite um numero real valido!\033[m\nDigite um numero: ')
        except KeyboardInterrupt:
            num = 0
            print(f'\033[0;31mO usuario decidiu deixar o espaço dos numeros reais vazio.\033[m')
            break
    return num