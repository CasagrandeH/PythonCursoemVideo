from classs004 import Escritor, Caneta, MaquinaDeEscrever
escritor = Escritor('Vagabunda')
caneta = Caneta('Faber castell')
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
print(escritor.nome)