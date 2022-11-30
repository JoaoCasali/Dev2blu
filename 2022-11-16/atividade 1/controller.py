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

def update(conta_update:Conta):
    lista_contas=[]
    contas = open("2022-11-16/atividade 1/contas.txt", "r") 
    for conta in contas:
        conta=conta.strip()
        contaObjeto = conta.split(";")
        if conta_update.numero == int(contaObjeto[1]):
            lista_contas.append(str(conta_update)+"\n")
        else:
            lista_contas.append(conta + '\n')
    contas.close()

    contas = open("2022-11-16/atividade 1/contas.txt", "w") 
    contas.writelines(lista_contas)
    contas.close()


def delete(conta_update:Conta):
    lista_contas=[]
    contas = open("2022-11-16/atividade 1/contas.txt", "r") 
    for conta in contas:
        conta=conta.strip()
        contaObjeto = conta.split(";")
        if conta_update.numero == int(contaObjeto[1]):
            pass
        else:
            lista_contas.append(conta + '\n')
    contas.close()

    contas = open("2022-11-16/atividade 1/contas.txt", "w") 
    contas.writelines(lista_contas)
    contas.close()
