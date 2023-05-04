dis = int(input('DISTANCIA:'))
print('='*60)
if dis <= 200:
    preço = dis * 0.50
    print('Como é uma viagem pequena sua passagem custaram {:.2f}R$'.format(preço))
else:
    preço = dis * 0.45
    print('Como é uma viagem mais longa custara {:.2f}R$.'.format(preço))
print('='*60)