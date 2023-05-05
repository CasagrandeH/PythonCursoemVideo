#metodos de adição

lista = ['Trento', 'Cacchorro quente', 'Arroz doce', 'Banana', 'Amendoin pelado']
print(f'A lista tem {len(lista)} itens, e ela é {lista}')
print('-'*50)
lista.append('Sorvete')
print(f'A lista agora tem {len(lista)} itens, e se tornou {lista}'
      f'\nPois foi adicionado Sorvete a lista, o metodo .append pode adicionar um item mas sempre o item sera colocado no final da lista')
print('-'*50)
lista.insert(0, 'Hamburguer')
print(f'A lista agora tem {len(lista)} itens, e se tornou {lista}'
      f'\nPois foi adicionado hamburguer a posição 0, o metodo .insert e para colocar o item por cima da posiçao desejada, '
      f'e então todos os outros itens irao se mover para o lado.')
print('-'*50)

#metodos de deleção

print('-'*50)
del(lista[0])
print(f'Agora a lista tem {len(lista)} itens, a lista se tornou {lista}'
      f'\nPois foi removido a posição 0 que era Hamburguer usando del(lista[0])'
      f'Os indices se reposicionar pra conpensar pelo item deletado.')
print('-'*50)
lista.pop(2)
print(f'Agora a lista tem {len(lista)} itens, e se tornou {lista}'
      f'\nPois foi removido a posição 2 que era Arroz doce usando lista.pop(2) '
      f'e entao de forma automatica os indices irao se reposicionar pra fechar a lacuna deixada pelo item 2'
      f'\nVale mencionar que lista.pop() iria remover o ultimo item automaticamente.')
print('-'*50)
lista.remove('Sorvete')
print(f'A lista agora tem {len(lista)} itens, e se tornou {lista}'
      f'\nPois o comando .remove acaba pedindo o item em si e não a posiçao em que ele se encontra, então o item e removido,'
      f'os indices se reposicionam tambem.')
print('-'*50)

#usando condiçoes

print('-'*50)
if 'Banana' in lista:
    lista.remove('Banana')
    print(f'A lista agora é {lista}')
else:
    print('A lista e a mesma pois Banana nao estava na lista')
print('-'*50)

#manipulando a ordem da lista

print('-'*50)
val = [8,3,8,2,3,10,9,11,1,0]
print(f'A lista é {val}.')
print('-'*50)
val.sort()
print(f'.sort ira organizar a lista de maior pra menor EX: \n{val}.')
print('-'*50)
val.sort(reverse = True)
print(f'Ja se voce quiser fazer o contrario vulgo, organizar a lista em ordem decrescente use o comando .sort(reverse = True) EX:\n{val}.')
print('-'*50)

#TOMAR CUIDADO

print('-'*50)
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,8]
print(f' A lista a: {a}.')
print('-'*50)
print(f'Após fazer b = a, na verdade oque acontece normalmente é a criação de uma copia da variavel que foi igualada.'
      f'\nMas quando a variavel é uma lista, fazer b = a irá linkar as duas listas EX:'
      f'\nb = a\n A lista a: {a}.\n A lista b: {b}.')
b = a
b[1] = 11
print(f'Agora que b = a aconteceu as listas serao:'
      f'\nb = a\nb[2] = 11\n A lista a: {a}.\n A lista b: {b}.'
      f'\nNote que as duas listas mudaram. ')
print('-'*50)
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
b = a[:]
b[2] = 11
print(f'Se voce quiser criar uma copia em vez de b = a voce deve escrever, b = a[:], pois entao b recebera todos valores de a e criara a copia. EX:'
      f'\nb = a[:]\n A lista a: {a}.\n A lista b: {b}.')
b[2] = 11
print(f'b[2] = 11\n A lista a: {a}.\n A lista b: {b}.')
print('-'*50)

#usando repetiçoes

print('-'*50)
valores = list(range(10,-1,-1))
print(f'Esse comando gerou a lista {valores}')
print('-'*50)
for c, num in enumerate(valores):
    print(f'Encontrei {num} na posição {c}')
print('-'*50)
for cont in range(0,5):
    valores.append(int(input('DIGITE UM VALOR: ')))
print(valores)
print('-'*50)

# MDS

ListaGeral = []
Notas = []
while True:
    Nome = str(input('Nome do Aluno: ')).capitalize()
    NotaUm = float(input('1ª Nota: '))
    NotaDois = float(input('2ª Nota: '))
    Alunos = [Nome, [NotaUm, NotaDois]]
    if Alunos[1] in Notas:
        Notas[Notas.index(Alunos[1])].append(Alunos[0])
    else:
        Notas.append(Alunos[1])
        ListaGeral.append(Alunos)
    print(f'ListaGeral: {ListaGeral}')
    print(f'ListaGeral[0]: {ListaGeral[0]}')
    print(f'ListaGeral[0][0]: {ListaGeral[0][0]}')
    print(f'ListaGeral[0][1]: {ListaGeral[0][1]}')
    print(f'ListaGeral[0][1][0]: {ListaGeral[0][1][0]}')
    rep = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if rep in 'Nn':
        break