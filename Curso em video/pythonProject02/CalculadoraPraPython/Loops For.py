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
print('''Esse código cria uma lista vazia e pede para o usuário digitar 5 valores numéricos, que serão adicionados à lista. Em seguida, ele usa dois loops "for" aninhados para comparar cada elemento da lista com o próximo elemento. Se o elemento atual for maior que o próximo elemento, os dois elementos serão trocados de lugar, colocando o menor antes do maior.

Isso é chamado de "ordenação por bolha", e o objetivo é organizar a lista em ordem crescente. O loop "for" externo garante que a comparação será feita para cada elemento da lista, enquanto o loop "for" interno faz as comparações de fato, trocando os elementos de posição conforme necessário.

No final, a lista é exibida na tela em ordem crescente.''')