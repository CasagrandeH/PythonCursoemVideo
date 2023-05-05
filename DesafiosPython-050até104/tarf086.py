Matris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        Matris[l][c] = int(input(f'Digite o valor de [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {Matris[l][c]:^5} ]', end= '')
    print()
print('-='*30)