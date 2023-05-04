frase = str(input('DIGITE UMA FRASE:'))
print('A LETRA <A> É USADA NA FRASE <{}> VEZES'.format(frase.lower().count('a')))
print('A PRIMEIRA INSTANCIA DE <A> SE ENCONTRA EM <{}>'.format(frase.lower().find('a')))
print('A ULTIMA INSTANCIA DE <A> SE ENCONTA EM <{}>'.format(frase.lower().rfind('a')))
