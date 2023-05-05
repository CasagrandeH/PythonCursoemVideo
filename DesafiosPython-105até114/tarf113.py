from tarefas.tarfs.MODULOS.utilidadesCEV import dados
numInt = dados.leiaInt(num=str(input('Digite um numero inteiro: ')))
numFloat = dados.leaiFloat(num=str(input('Digite um numero real: ')))
print(f'O numero inteiro digitado foi {numInt} e o numero real {numFloat}.')