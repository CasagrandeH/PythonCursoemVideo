def voto(ano):
    '''
    -> Calcula a sua idade e te diz sua situação de eleitor.
    :param ano: Ano de nascimento do usuario que e então usado pra calcular sua idade
    :return: a idade, a sua obrigação eleitoral
    '''
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - ano
    if 18 <= idade < 65:
        return  f'Com idade {idade}: VOTO É OBRIGATORIO'
    elif 16 <= idade < 18 or idade >= 65:
        return  f'Com idade {idade}: VOTO É OPCIONAL'
    else:
        return  f'Com idade {idade}: NÃO VOTA'


ano = int(input('Em que ano você nasceu?: '))
print(voto(ano))
