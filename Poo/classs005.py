class CarrinhoDeCompras:

    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(f'O produto {produto.nome} custa {produto.preço}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'R${total:.2f}'.replace('.',',')

class Produto:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.preço = f'R${valor:.2f}'.replace('.',',')