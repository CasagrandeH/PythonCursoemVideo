LinhaZero = []
LinhaUm= []
LinhaDois = []
Total = []
Par = 0
for c in range(0,3):
    Num = int(input(f'Digite o valor de [0,{c}]: '))
    LinhaZero.append(Num)
for c in range(0,3):
    Num = int(input(f'Digite o valor de [1,{c}]: '))
    LinhaUm.append(Num)
for c in range(0,3):
    Num = int(input(f'Digite o valor de [2,{c}]: '))
    LinhaDois.append(Num)
Total.append([LinhaZero, LinhaUm, LinhaDois])
for Linhas in Total:
    for Linha in Linhas:
        for Numero in Linha:
            if Numero % 2 == 0:
                Par += Numero
print('-='*30)
print(f'[ {LinhaZero[0]:^5} ][ {LinhaZero[1]:^5} ][ {LinhaZero[2]:^5} ]')
print(f'[ {LinhaUm[0]:^5} ][ {LinhaUm[1]:^5} ][ {LinhaUm[2]:^5} ]')
print(f'[ {LinhaDois[0]:^5} ][ {LinhaDois[1]:^5} ][ {LinhaDois[2]:^5} ]')
print('-='*30)
print(f'A soma dos numeros pares é {Par}.')
print('-'*60)
print(f'A soma dos valores da 3ª coluna é {LinhaZero[2] + LinhaUm[2] + LinhaDois[2]}')
print('-'*60)
print(f'O maior valor da 2ª linha é: {max(LinhaUm)}.')
print('-='*30)
print('\nEND.')
