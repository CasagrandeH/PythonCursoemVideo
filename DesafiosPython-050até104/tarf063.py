num_inicial = int(input('QUAL NUMERO?:'))
qtd_elementos = int(input('QUANTOS ELEMENTOS?:'))
num_anterior = num_inicial
num_atual = num_anterior + 1
count = 2
print(num_anterior, end= '')
print(num_atual, end= '')
while count < qtd_elementos:
    prox_num = num_anterior + num_atual
    print('[{:^11}]'.format(prox_num), end= '')
    num_anterior = num_atual
    num_atual = prox_num
    count += 1
print('Fim.')