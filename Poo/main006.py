from classs006 import Clientes, Enderecos

c1 = Clientes('Gustavo', 21)
c1.insere_endereço('Cacoal', 'RO')
c2 = Clientes('Maria', 44)
c2.insere_endereço('Salvador', 'Bahia')
c2.insere_endereço('Rio de Janeiro', 'RJ')
print(c1.nome, end= ' ')
c1.lista_enderecos()
print(c2.nome, end= ' ')
c2.lista_enderecos()
