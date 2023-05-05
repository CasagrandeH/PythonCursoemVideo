from tarefas.tarfs.MODULOS import moeda

n = int(input('Digite um valor: '))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'Com desconto de 10%, o valor fica {moeda.diminuir(n, 10, True)}')
print(f'Com juros de 20%, o valor fica {moeda.aumentar(n, 20, True)}')
print(f'Com juros de 30%, o valor fica {moeda.aumentar(n, 30)}')