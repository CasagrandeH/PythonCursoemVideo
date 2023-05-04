c = 1
idade_maior = homem = mulher_menos = 0
while True:
    print(f'---CANDIDATO {c}---\n')
    idade = int(input('IDADE: '))
    sexo = input('SEXO ( M / F ): ').strip().upper()[0]
    while sexo not in ['M', 'F']:
        sexo = input('Input invalido.\nSEXO ( M / F ): ').strip().upper()[0]
    if idade > 18:
        idade_maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menos += 1
    continuar = input('\nContinuar? ( S / N ): \n').strip().upper()[0]
    while continuar not in ['S', 'N']:
        continuar = input('\nInput invalido.\nContinuar? ( S / N ): \n').strip().upper()[0]
    if continuar == 'N':
        break
    else:
        c += 1
print(f'''[ {idade_maior} ] pesoas tem mais de 18 anos.
Foram cadastrados [ {homem} ] homens.
[ {mulher_menos} ] mulheres tem menos que 20 anos de idade.''')
