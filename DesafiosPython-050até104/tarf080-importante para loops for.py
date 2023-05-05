lista = []
for pos in range(0,5):
    valor = int(input('DIGITE UM VALOR: '))
    lista.append(valor)
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(f'A lista gerada foi: {lista}')
#versao do fessor
'''lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]
                lista.insert(pos, n)
                break
            pos += 1
print(f'A lista em ordem crescente sem usar .sort ficou: {lista}')'''