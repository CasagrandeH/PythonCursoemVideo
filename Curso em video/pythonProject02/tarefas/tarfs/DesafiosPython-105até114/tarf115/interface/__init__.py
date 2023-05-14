from tarefas.tarfs.tarf115.arquivo import *


def linha(tam=42):
    return '-'*tam


def titulo(msg=''):
    print(linha())
    print(f'\033[0;35m{msg:^42}\033[m')
    print(linha())


def colorido(msg, cor=0, op=False):
    if not op:
        print(f'\033[0;3{cor}m', end='')
        print(msg, end='')
        print(f'\033[m', end='')
    else:
        print(f'\033[0;3{cor}m', end='')
        print(msg, end='')
        print(f'\033[m', end='')
        num = int(input(''))
        return num


def menu():
    titulo('MENU PRINCIPAL')
    colorido(msg='1', cor=3), colorido(msg=' - ', cor=2), colorido(msg=' Ver pessoas cadastradas', cor=4)
    colorido(msg='\n2', cor=3), colorido(msg=' - ', cor=2), colorido(msg=' Cadastrar nova pessoa', cor=4)
    colorido(msg='\n3', cor=3), colorido(msg=' - ', cor=2), colorido(msg=' Sair do sistema', cor=4)
    print()


def opção():
    while True:
        try:
            op = colorido(msg='Sua opção > ', cor=3, op=True)
            op = int(op)
            if op == 3:
                titulo('Saindo do sistema... Até logo!')
                return op
                break
            elif op == 2:
                titulo('Opção 2')
                adicionarInfo('cursoemvideo.txt')
                return op
            elif op == 1:
                titulo('Opção 1')
                lerArquivo('cursoemvideo.txt')
                return op
            else:
                colorido(msg='ERRO: Por favor digite uma opção valida.\n', cor=1)
        except (ValueError, TypeError):
            colorido(msg='ERRO: Por favor digite um numero inteiro.\n', cor=1)

