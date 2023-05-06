from time import sleep
from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.now().year)

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        sleep(1)
        print(f'Você mandou {self.nome} começar a falar sobre {assunto}:')
        if self.comendo:
            print(f'    -> {self.nome} prefere não falar enquanto come.')
            return

        if self.falando:
            print(f'    -> {self.nome} ja esta falando.')
            return

        self.falando = True
        print(f'    -> {self.nome} esta falando sobre {assunto}.')

    def parar_falar(self):
        sleep(1)
        print(f'Você mandou {self.nome} parar de falar.')
        if not self.falando:
            print(f'    -> {self.nome} não estava falando.')
            return

        self.falando = False
        print(f'    -> {self.nome} parou de falar.')

    def comer(self, alimento):
        sleep(1)
        print(f'Você mandou {self.nome} comer {alimento}.')
        if self.comendo:
            print(f'    -> {self.nome} ja esta comendo.')
            return

        if self.falando:
            print(f'    -> {self.nome} não quer comer agora, pois ainda esta falando.')
            return

        print(f'    -> {self.nome} esta comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        sleep(1)
        print(f'Você mandou {self.nome} parar de comer.')
        if not self.comendo:
            print(f'    -> {self.nome} não estava comendo.')
            return

        self.comendo = False
        print(f'    -> {self.nome} parou de comer.')


    def get_ano_nascimento(self):
        sleep(1)
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade, falando=False, comendo=False)

    @staticmethod
    def gerar_id():
        rand = randint(1000, 1999)
        return rand

class Produto:

    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def desconto(self, percentual):
        self.preço = self.preço - (self.preço * (percentual / 100))

    #getter
    @property
    def preço(self):
        return self._preço

    #setter
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preço = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, val):
        self._nome = val.title()
