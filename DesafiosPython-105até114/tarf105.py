def notas(lista=0):
    '''
    -> função para analisar notas e situaçoes de varios alunos.
    :param lista: uma ou mais notas dos alunos
    :return: dicionario com varias informaçoes sobre a situação da turma
    '''
    ficha = {}
    ficha['cadastros'] = len(lista)
    ficha['maior'] = max(lista)
    ficha['menor'] = min(lista)
    ficha['media'] = sum(lista) / len(lista)
    if ficha['media'] >= 7:
        ficha['situação'] = 'BOA'
    elif 7 < ficha['media'] >= 6:
        ficha['situação'] = 'RAZOÁVEL'
    else:
        ficha['situação'] = 'RUIM'
    print('-'*50)
    print(ficha)


tudo = []
while True:
    nota = float(input('Nota: '))
    tudo.append(nota)
    rep = str(input('Continuar?: ')).strip().upper()[0]
    if rep in 'N':
        break
notas(tudo)
