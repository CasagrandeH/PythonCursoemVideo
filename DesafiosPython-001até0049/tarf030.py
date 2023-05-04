n = int(input('Digite um numero:'))
print('='*60)
#even = '0' in n[len(n)-1], '2' in n[len(n)-1], '4' in n[len(n)-1], '6' in n[len(n)-1], '8' in n[len(n)-1]
#odd = '1' in n[len(n)-1], '3' in n[len(n)-1], '5' in n[len(n)-1], '7' in n[len(n)-1], '9' in n[len(n)-1]
if (n % 2) == 0:
    print('O numero é par.')
else:
    print('O numero é impar')
print('='*60)