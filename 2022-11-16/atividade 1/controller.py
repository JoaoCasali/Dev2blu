from model import Conta
def create(contas):
    arquivo = open("2022-11-16/atividade 1/contas.txt", "w")
    for conta in contas:
        arquivo.write(f"{conta}\n")

    arquivo.close()    

def read():
    lista = []
    arquivo = open("2022-11-16/atividade 1/contas.txt", "r")
    for conta in arquivo:
        conta = conta.strip("\n")
        conta = conta.split("; ")
        lista.append(Conta(conta[0], conta[1], conta[2]))

    arquivo.close()
    return lista