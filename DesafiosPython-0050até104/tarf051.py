a = int(input('PRIMEIRO TERMO'))
r = int(input('RAZÃO:'))
d = a + (10 - 1) * r # d = ATE QUAL POSIÇAO IRA
for c in range(a, d, r):
    print('{}'.format(c), end= '-> ')