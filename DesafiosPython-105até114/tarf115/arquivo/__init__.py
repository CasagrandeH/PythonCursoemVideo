from tarefas.tarfs.tarf115.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print('Arquivo txt criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()


def adicionarInfo(arq):
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    with open(arq, 'a+') as arquivo:
        arquivo.seek(0, 2)  # posicionar o cursor no final do arquivo
        if arquivo.tell() > 0:
            arquivo.seek(arquivo.tell() - 1)  # posicionar o cursor no último caractere
            ultimo_caractere = arquivo.read(1)  # ler o último caractere
            if ultimo_caractere != '\n':
                arquivo.write('\n')  # adicionar quebra de linha
        arquivo.write(f'{nome:<35}{idade} anos')
