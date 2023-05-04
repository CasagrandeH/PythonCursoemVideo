produtos = []
total = maisde_mil = entrada = 0
while True:
    entrada += 1
    print(f'---ENTRADA {entrada}---\n')
    nome = input('Qual o nome do produto?: ').capitalize()
    while True:
        try:
            preço_p = float(input('Qual o preço do produto?: '))
            break
        except ValueError:
            print('Valor inválido. Digite um número válido.')
    total += preço_p
    if preço_p > 1000:
        maisde_mil += 1
    produtos.append((nome, preço_p))
    if len(produtos) == 0:
        print('Nenhum produto foi cadastrado.')
    else:
        produto_maisbarato = produtos[0]
        for produto_ in produtos:
            if produto_[1] < produto_maisbarato[1]:
                produto_maisbarato = produto_
    continuar = input('Continuar? ( S / N ): ').strip().upper()[0]
    while continuar not in ['S', 'N']:
        continuar = input('Input invalido. Digite novamente.\nContinuar? ( S / N ): ').strip().upper()[0]
    if continuar == 'N':
        break
for produto_ in produtos:
    print('\n')
    print(f'NOME: {produto_[0]}')
    print(f'PREÇO: {produto_[1]:.2f}')
print(f'O total gasto foi de [ {total:.2f} ]')
print(f'Temos {maisde_mil} produtos custando mais de mil reais.')
print(f'O produto mais barato é {produto_maisbarato[0]}, que custa [ {produto_maisbarato[1]:.2f} ]')
