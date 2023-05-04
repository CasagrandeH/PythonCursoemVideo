r1 = float(input('RETA 1:'))
r2 = float(input('RETA 2:'))
r3 = float(input('RETA 3:'))
if r1>r2 and r1>r3:
    cal = r2 + r3
    maior = r1
if r2>r1 and r2>r3:
    cal = r1 + r3
    maior = r2
if r3>r1 and r3>r2:
    cal = r1 + r2
    maior = r3
if cal > maior:
    print('As retas podem formar um triangulo.')
else:
    print('As retas não podem formar um triangulo.')
print(cal , maior)
#VERSAO do PROF
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triangulo.')
else:
    print('As retas NAO podem formar um triangulo.')
