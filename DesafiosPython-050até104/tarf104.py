def leiaInt(num):
    while not num.isnumeric():
        num = leiaInt(input('Valor invalido! Digite um numero inteiro valido!\nDigite um numero: '))
    return num

n = leiaInt(input('Digite um numero: '))
print(f'Você acabou de digitar o numero [{n}].')