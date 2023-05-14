from tarefas.tarfs.MODULOS.utilidadesCEV import moeda
num = float(input('Valor: R$'))
moeda.resumo(num, 80, 35, dob=True, met=True)