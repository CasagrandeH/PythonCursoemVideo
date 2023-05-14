from tarefas.tarfs.MODULOS.utilidadesCEV import moeda, dados

num= dados.leiaDenero(str(input('Valor: R$')))
moeda.resumo(num, 80, 35, dob=True, met=True)