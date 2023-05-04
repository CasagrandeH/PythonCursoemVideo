r1 = float(input('RETA 1:'))
r2 = float(input('RETA 2:'))
r3 = float(input('RETA 3:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triangulo.')
    if r1 == r2 == r3:
        print('Este é um triangulo EQUILATERO.')
    elif r1 == r2 and r2 != r3 or r2 == r3 and r1 != r2:
        print('Este triangulo é ISÓSCELES.')
    elif r1 != r2 != r3:
        print('Este triangulo é ESCALENO.')
else:
    print('As retas NAO podem formar um triangulo.')
