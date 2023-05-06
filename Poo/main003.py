from classs003 import Base_de_dados
bd = Base_de_dados()
bd.inserir_cliente(1, 'Gustavo')
bd.inserir_cliente(2, 'Guilherme')
bd.inserir_cliente(3, 'Diaz')
bd.lista_clientes()
print('-'*30)
bd.apaga_cliente(3)
bd.lista_clientes()