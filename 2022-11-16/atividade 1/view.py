from controller import create, read, update, delete
from model import Conta

# lista_contas = []

# lista_contas.append(Conta("Joao", "54213", 1200))
# lista_contas.append(Conta("Nicolas", "12321", 1400))
# lista_contas.append(Conta("Carlos", "12512", 1500))
# create(lista_contas)

delete(Conta(
    "André",
    12321,
    1400
))