peso = float(input('Qual seu peso:'))
alt = float(input('Qual sua altura em metros:'))
imc = peso / (alt ** 2)
print('{:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade morbida.')
