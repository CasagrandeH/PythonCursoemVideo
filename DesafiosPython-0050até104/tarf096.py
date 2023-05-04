def área(a, b):
    area = a * b
    print('-'*30)
    print(f'A área de um terreno {a} x {b} é {area}m²')
    print('-' * 30)


#Programa principal
print('Controle de Terrenos')
print('-='*15)
while True:
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    área(largura, comprimento)
    rep = str(input('Continuar? (s/n): ')).strip().upper()[0]
    if rep in 'N':
        print('\nEND.')
        break
