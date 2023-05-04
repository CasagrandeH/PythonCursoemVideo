origem = str(input('DIGITE UMA FRASE:')).strip.upper
reformatação = origem.split()
rem_ = ''.join(reformatação)
print('[ {} ] é o resultado quando se remove os espaços na string \n[ {} ] é a quantidade de letras na frase'.format(rem_, tamanho))
'''invertido = rem_[::-1]'''#JEITO DO PROFESSOR PRA DIMINUIR O CODIGO
invertido = ''# ISSO É O EQUIVALENTE DE invertido = 0[mas nesse caso um e para string e o outro numeros]
for letra in range(len(rem_) - 1, - 1, -1):
    invertido += rem_[letra]
print('[ {}, {} ]'.format(rem_, invertido))
print(len(invertido))
if rem_ == invertido:
    print('Esta frase é um palíndromo.')
else:
    print('Esta frase não é um palindromo')
print('FIM.')

