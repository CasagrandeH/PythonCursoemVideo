from re import match
from ast import parse
expressão = [input('Digite uma expressão matematica: ')]
if match('^[0-9\+\-\*\/().\s]+$', expressão[0]):
    try:
        parse(expressão[0])
        result = eval(expressão[0])
        print(f'A expressão é {result}.')
    except SyntaxError:
        print('A expressão é invalida.')
else:
    print('A expressão é invalida.')