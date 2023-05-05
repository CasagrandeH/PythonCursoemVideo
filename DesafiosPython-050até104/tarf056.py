total = 0
nomeV = 0
novaM = 0
homem = 0
nomeF = ''
for c in range(1,5):
    nome = input('QUAL O NOME DO INDIVIDUO:')
    idade = int(input('QUAL A IDADE DE {}?:'.format(nome.upper())))
    sexo = int(input('0 = HOMEM \n1 = MULHER'))
    total += idade
    if c == 1:
        if sexo == 0:
            nomeV = idade
            nomeF = nome
            homem += 1
        if sexo == 1:
            if idade < 20:
                novaM += 1
    else:
        if sexo == 0:
            if idade > nomeV:
                nomeV = idade
                nomeF = nome
                homem += 1
        if sexo == 1:
            if idade < 20:
                novaM += 1
    media = total / 4
print('A média da idade de todos é {}.'.format(media))
if homem >= 1:
    print('O homem mais velho se chama {}.'.format(nomeF))
else:
    print('Não Há homens.')
if novaM >= 1:
    print('No grupo há {} mulheres abaixo de 20 anos de idade:'.format(novaM))
else:
    print('Não há mulheres.')
