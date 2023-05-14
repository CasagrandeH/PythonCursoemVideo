from tarefas.tarfs.MODULOS import moeda

n = int(input('Digite um valor: '))
print(f'O dobro de R${n} é R${moeda.dobro(n):.2f}')
print(f'A metade de R${n} é R${moeda.metade(n):.2f}')
print(f'Com desconto de 10%, o valor fica R${moeda.diminuir(n, 10):.2f}')
print(f'Com juros de 20%, o valor fica R${moeda.aumentar(n, 20):.2f}')