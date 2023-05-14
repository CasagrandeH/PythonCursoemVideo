import requests
url = "http://pudim.com.br"
try:
    resposta = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f'\033[0;31mNão foi possivel acessar o site pudim no momento.\033[m')
else:
    if resposta.status_code == 200:
        print('\033[0;32mConexão bem-sucedida! O site Pudim está acessível.\033[m')
    else:
        print(f'\033[0;31mO site Pudim esta indisponivel no momento\033[m')
finally:
    print('Volte sempre!')
