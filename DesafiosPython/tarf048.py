s = 0
ss = 0
for c in range(1 ,501 ,2):
    if c % 3 == 0:
        s += c
        ss = c + 1
print('soma {}'.format(s))
print('vezes contadas {}'.format(ss))
print(c)
