from re import match
from ast import parse
expressão = [input('Digite uma expressão matematica: ')]
if match('^[0-9\+\-\*\/().\s]+$', expressão[0]):
    try:
        parse(expressão[0])
        print(f'A expressão é valida.')
    except SyntaxError:
        print('A expressão é invalida.')
else:
    print('A expressão é invalida.')
#modo sem listas
expr = str(input('Digite sua expressão: '))
if expr.count('(') == expr.count(')'):
	print('Sua expressão é válida')
else:
	print('Sua expressão não é válida')