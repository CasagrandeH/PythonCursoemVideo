n1 = int(input('NUMERO 1:'))
n2 = int(input('NUMERO 2:'))
n3 = int(input('NUMERO 3:'))
'''if n1>n2 and n1>n2:
    print('O maior numero é {}'.format(n1))
if n2>n1 and n2>n3:
     print('O maior numero é {}'.format(n2))
if n3>n1 and n3>n2:
    print('O maior numero é {}'.format(n3))
if n2 > n1 and n1<n3:
    print('O menor numero é {}'.format(n1))
if n2<n1 and n2<n3:
    print('O menor numero é {}'.format())
if n3<n1 and n3<n2:
    print('O menor numero é {}'.format(n3))'''
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n2
if n1>n2 and n1>n3:
    maior = n1
if n3>n1 and n3>n2:
    maior = n3
print('Menor {}'.format(menor))
print('Maior {}'.format(maior))