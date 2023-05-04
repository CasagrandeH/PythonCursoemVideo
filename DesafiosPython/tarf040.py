print('CALCULE SUA MÉDIA:')
n1 = float(input('NOTA 1:'))
n2 = float(input('NOTA 2:'))
media = (n1 + n2) / 2
if media < 5.0:
    print('Infelizmente como sua média foi {}, fostes reprovado.'.format(media))
elif media > 5.0 and media < 7.0: #elif 7.0 > media >= 5.0:
    print('Como a sua média ficou um pouco abaixo do esperado você ficara de recuperação.')
elif media > 7.0:
    print('VOCÊ FOI APROVADO!!!!')
print(media)