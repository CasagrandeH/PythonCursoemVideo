from random import shuffle, sample
a1 =input('ALuno1:')
a2 =input('Aluno2:')
a3 =input('ALuno3:')
a4 =input('ALuno4:')
l = [a1,a2,a3,a4]
print('{}.'.format(sample([a1,a2,a3,a4], k=4)))
shuffle(l)
print('A ordem de apresentação será:')
print(l)
