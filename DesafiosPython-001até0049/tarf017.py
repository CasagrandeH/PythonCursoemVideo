from math import hypot
co =float(input('Qual o valor do cateto oposto?:'))
ca =float(input('Qual o valor do cateto adjacente?:'))
#print('O valor da hipotenusa é {:.2f}.'.format(math.hypot(co,ca)))
h = (co**2+ca**2)**(1/2)
print('A hipotenusa é {:.2f}'.format(h))
