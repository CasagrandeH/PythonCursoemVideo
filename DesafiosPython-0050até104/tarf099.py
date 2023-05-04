def maior(*num):
    print('-=' * 30)
    if len(num) == 0:
        print(f'Não foram registrados numeros.')
    else:
        for c in num:
            print(f'{c}', end= ' ')
            sleep(0.4)
        print(f'Foram informados {len(num)} valores.')
        for pos, c in enumerate(num):
            if pos == 0:
                mai = c
            elif c > mai:
                mai = c
        print(f'Entre os numeros, {mai} é o maior.')


#programa principal
from time import sleep
maior(2,1,2,3,4,5,2,2,7)
maior(44,123,7,65,89,1)
maior(484,122)
maior()