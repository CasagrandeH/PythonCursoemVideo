num = count = total = 0
num = int(input('( [999] para parar )NUMERO: '))
while num != 999:
    total += num
    count += 1
    num = int(input('( [999] para parar )NUMERO: '))
print('A soma de todos os numeros digitados é {}. Foram digitados {} numeros.'.format(total, count))