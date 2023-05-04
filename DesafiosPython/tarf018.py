from math import sin, cos, tan, radians
a =float(input('Qual o valor do angulo?:'))
r = radians(a)
print('O sêno é {:.2f}, o cosseno {:.2f}, e a tangente {:.2f}.'.format(sin(r), cos(r), tan(r)))
