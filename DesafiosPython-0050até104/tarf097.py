def escreva(msg):
    tam = len(msg)
    print(f'~'* tam)
    print(f'{msg:^{tam}}')
    print(f'~' * tam)


#programa principal
escreva('OU, SEU BUNDA MOLE!')
escreva('FALOU COMIGO?')
escreva('NÃO, FALEI COM A PUTA QUE TE PARIU!')
escreva('AINDA BEM, ATÉ UM OUTRO DIA.')
escreva(msg = str(input('Mensagem: ')))
print('\nFIM.')