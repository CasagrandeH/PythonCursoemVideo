from random import randint
from time import sleep, time
from math import ceil
jogar_novamente = True
while jogar_novamente:
    # CPU escolhe um numero de 1 a 10
    com = randint(1,10)
    # Variaveis iniciaveis
    play = 0
    count = 0
    choice = 0
    choices = 0
    pontos = 100
    # Instruçoes do jogo
    print('Meu nome é cpu, estou pensando em um numero de 1 a 10.\nTente adivinha-lo.')
    sleep(0.5)
    tentativas = int(input('Vou deixar você escolher quantas tentativas você terá!\nQUAL O NUMERO DE TENTATIVAS:'))
    tempo = float(input('Agora escolha quanto tempo você gostaria de ter.\nQUANTO TEMPO: '))
    print('Você começa com 100 pontos.\nSe pedir uma dica serão descontados pontos de acordo com o nivel de dificuldade escolhido.\nPS: APÓS TODA TENTATIVA SERA PERGUNTADO SE QUER UMA DICA 1 = SIM | 2 = NÃO')
    acertou = False
    print('.', end='')
    print('.', end='')
    print('.')
    # Game loop
    tentativas_restantes = tentativas
    tempo_inicial = time()
    while not acertou and pontos > 0 and tentativas_restantes > 0:
        play = int(input('O NUMERO É: '))
        try:
            tentativas_restantes -= 1
            count += 1
            if play == com:
                acertou = True
            else:
                choice = int(input('EROOOOOOU! TENTE NOVAMENTE!\nQuer uma dica?\n(Lembre-se que usar dicas desconta pontos!!!)\n[ 1 ] = SIM\n[ 2 ] = NÃO'))
                if choice == 1:
                    choices += 1
                    if play > com:
                        print('O numero dado foi maior do que o que pensei.')
                    else:
                        print('O numero dado foi menor do que o que pensei.')
                elif choice not in [1, 2]:
                    print('INVALIDO.')
                    continue
        except ValueError:
            print('Precisa escolher um numero inteiro.')
            continue
        # Checando se o jogador ganhou ou perdeu e imprimindo o resultado
        tempo_final = time()
        tempo_total = tempo_final - tempo_inicial
        tentou = tentativas - count
        fator_escala = 10
        if tentou <= 0:
            tentou = 1
        if tempo_total > tempo:
            penalidade = ((tentou * (tempo_total - tempo))) + (10 * choices)
            pontos = pontos - penalidade * fator_escala
        else:
            penalidade = ((tentou * (tempo - tempo_total))) - (10 * choices)
            pontos = pontos + penalidade * fator_escala
    if tentativas_restantes == 0:
        print('Você PERDEU. o numero era {}'.format(com))
    else:
        print('Acertou em [ {} ] tentativas!\n[ {} ] pontos!\nDê [ {:.2f} ] você levou [ {:.2f} ] segundos!\nO numero era [ {} ]!'.format(count, ceil(pontos), tempo, tempo_total, com))
    sleep(3)
    jogar_novamente = input('Quer jogar de novo? (S/N): ').strip().upper()
    while jogar_novamente not in ['S', 'N']:
        print('Resposta inválida, tente novamente.')
        jogar_novamente = input('Quer jogar de novo? (S/N): ').strip().upper()
    jogar_novamente = jogar_novamente == 'S'
    print('\n','-='*30)
print('Fim.')
