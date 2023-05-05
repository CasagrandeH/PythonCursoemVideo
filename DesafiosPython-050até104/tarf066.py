c = s = 0
while True:
    num = int(input(f'--- NUMERO {c+1} ---\n'))
    if num == 999:
        break
    s += num
    c += 1
print(f'A soma desses {c} numeros é {s}')