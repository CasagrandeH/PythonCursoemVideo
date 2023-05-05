#ANALISE DOS CARACTERES ENCONTRADOS NA SUA STRING
frase = 'Curso em Video python'
f1 = frase
print(frase,f1)
print('Qual o tamanho da string:',len(frase))
n = str(input('Analisar quantos desta letra há:'))
print(frase.count(n))
#LOCALIZAR INFORMAÇÃO NA STRING

n1 = str(input('Localizar:'))
print('O item procurado se localiza na posição :{}'.format(frase.find(n1)))
#LOCALIZAR SE A STRING EXISTE NA STRING COM TRUE/FALSE
m = str(input('Qual objeto localizar?:'))
print( m in frase)
#==========================================================================
n2 = str(input('Reforma desejada:'))
n3 = frase.replace('Video python',n2)
#==========================================================================

#print(frase.upper())
ma = n3.upper()
print('Upper cased: {}'.format(ma))
#print(frase.lower())
mb = n3.lower()
print('Lower cased: {}'.format(mb))
#print(frase.capitalize())
mc = n3.capitalize()
print('Capitalizado: {}'.format(mc))
#print(frase.title())
md = n3.title()
print('Como se fosse titulo: {}'.format(mc))

#FORMATAÇÃO DE STRING
texto = '   Aprenda python  '
print(texto)
t = texto.strip()
print('__'+t+'__')
t1 = texto.rstrip()
print(t1+'__')
t2 = texto.lstrip()
print('__'+t2)
print(len(texto))
print(texto[0:10]+texto[11:])

#QUEBRAR UMA LISTA EM VARIAS LISTAS DE ACORDO COM O NUMERO DE ESPAÇAMENTOS NA STRING
frase.split()
s = '_'.join(frase)
print(s)

#COMO INVERTER UMA STRING
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
