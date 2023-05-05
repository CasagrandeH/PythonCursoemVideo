sala = float(input('Qual o salário do funcionario:'))
if sala <= 1250.00:
    aum = sala * ( 15 / 100 )
else:
    aum = sala * ( 10 / 100 )
novo = sala + aum
print(' O salario aumentou para {:.2f}R$'.format(novo))