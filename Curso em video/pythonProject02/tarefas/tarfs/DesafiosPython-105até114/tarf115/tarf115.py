from tarefas.tarfs.tarf115.interface import *
from tarefas.tarfs.tarf115.arquivo import *

arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    menu()
    print(linha())
    op = opção()
    if op == 3:
        break