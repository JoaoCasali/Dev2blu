from controller import create, read
from model import Conta

lista_contas = []

lista_contas.append(Conta("Joao", "12321", 1200))
lista_contas.append(Conta("Nicoals", "12321", 1400))
create(lista_contas)