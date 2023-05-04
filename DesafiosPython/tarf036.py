valor = float(input('Valor da casa:'))
sal = float(input('O seu salário:'))
anos = float(input('Em quantos anos sera pago'))
pres = valor / (anos * 12)
if pres > sal * (30 / 100):
    print('O emprestimo infelizmente não pode ser realizado, agradecemos a compreensão.')
else:
    print('O empréstimo é possivel.')
