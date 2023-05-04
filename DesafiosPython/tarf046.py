from datetime import date
from time import sleep
for c in range(10,0,-1):
    print('{}!'.format(c))
    sleep(1)
print('Feliz {}!'.format(date.today().year))
