Tupla = ()
print('Para sair do programa digite [ STOP ].')
while True:
    Palavra = str(input('DIGITE UMA PALAVRA: ')).strip().upper()
    if Palavra in 'STOP':
        break
    while not Palavra.isalpha():
        Palavra = str(input('INVALIDO!\nDIGITE UMA PALAVRA: ')).strip().upper()
    for p in Palavra:
        if p.lower() in 'aeiou':
            Vogais.append(p.lower(), )
    Vogais = ' '.join(Vogais)
    Tupla += (Palavra, Vogais, )
    Vogais = []
for pos, p in enumerate(Tupla):
    if pos % 2 == 0:
         print(f'Na palavra {Tupla[pos]} temos,', end= ' ')
    elif pos % 2 != 0:
        print(f'{Tupla[pos]}')
#Versao do fessor
'''Tupla = ('aprender', 'localizar', 'mamar', 'lambuzar'
            'etc')
for p in Tupla:
    print(f'\nNa palavra {p} temos ', end= '')
    for Letra in p:
        if Letra.lower() in 'aeiou':
            print(f'{Letra}', end= ' ')'''
