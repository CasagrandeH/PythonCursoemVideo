preço = float(input('O preço do produto em reais:'))
print('-='*30)
print('ESCOLHA A FORMA DE PAGAMENTO:')
sel = int(input('1 = DINHEIRO/CHEQUE \n2 = CARTÃO DE DEBITO \n3 = EM 2X NO CARTÃO \n4 = EM 3X NO CARTÃO'))
print('-='*30)
if sel == 1:
    des = preço * (10/100)
    des_f = preço - des
    print('O preço foi de {}R$ para {}R$, pois em pagamento em dinheiro/cheque há 10% de desconto.'.format(preço, des_f))
elif sel == 2:
    des = preço * (5/100)
    des_f = preço - des
    print('O preço foi de {}R$ para {}R$, pois em pagamento em pagamento dem cartão de débito há 5% de desconto.'.format(preço, des_f))
elif sel == 3:
    par = preço / 2
    print('O preço é {}R$, então a parcela fica {}R$ pois em 2x no cartão não há descontos.'.format(preço, par))
elif sel == 4:
    juros = preço * (20/100)
    preço_f = preço + juros
    par = preço_f / 3
    print('O preço vai de {}R$ para {}R$, com uma parcela de 3x de {}R$, pois pago em 3x há juros de 20%.'.format(preço, preço_f, par))
