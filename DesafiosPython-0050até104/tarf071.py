cinquenta = vinte = dez = um = 0
print('='*57)
print('{:<1}{:^53}{:>1}'.format('||', 'BANCO GRANDAU', '||'))
print('='*57)
num = int(input('Quantos quer sacar?: R$'))
while True:
	if num >= 50:
		num -= 50
		cinquenta += 1
	elif num >= 20:
		num -= 20
		vinte += 1
	elif num >= 10:
		num -= 10
		dez += 1
	elif num >= 1:
		num -= 1
		um += 1
	if num == 0:
		break
print('Foram retiradas {} cédulas de R$50'.format(cinquenta))
print('Foram retiradas {} cédulas de R$20'.format(vinte))
print('Foram retiradas {} cédulas de R$10'.format(dez))
print('Foram retiradas {} cédulas de R$1'.format(um))
print('='*57)
print('{:<1}{:^53}{:>1}'.format('||', 'Tenha um bom dia e volte sempre ao banco do Grande!', '||'))
print('='*57)
