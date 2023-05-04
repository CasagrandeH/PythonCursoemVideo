def fatorial(num=1, show= False):
    '''
    MOSTRA O FATORIAL DE UM NUMERO
    :param num: (opcional) numero a ser fatorado
    :param show: (opcional) para mostrar a conta que foi feita
    :return: (f) resultado do fatorial, (conta) conta do fatorial EX: 5x4x3x2x1 =
    '''
    f = 1
    conta = []
    for c in range(num, 0, -1):
        f *= c
        if show is True:
            conta.append(c)
    if conta == []:
        return f
    else:
        return f, conta

print(fatorial(5))
for c in fatorial(7, show= True)[1]:
    if c == 1:
        print(f'{c}', end=' = ')
    else:
        print(f'{c}', end= ' x ')
print(f'{fatorial(7)}\n')
print(fatorial())
print(fatorial(show= True))