def create(path, contas):
    arquivo = open(path, "w")
    for conta in contas:
        arquivo.write(f"{conta}\n")

    arquivo.close()    

def read(path, Tipo):
    lista = []
    arquivo = open(path, "r")

    for conta in arquivo:
        conta = conta.strip("\n")
        conta = conta.split(";")

        pessoa = Tipo(conta[2], conta[3], conta[4])
        pessoa.segundo_titular = conta[5]
        lista.append(pessoa)

    arquivo.close()
    return lista

def update(contas, indice, Tipo, path):
    contas[indice] = Tipo(
        str(input("Digite o Nome do 1° titular:> ")).strip(),
        str(input("Digite o codigo:> ")),
        float(input("Digite o Saldo Inicial:> "))
    )

    create(path, contas)

def delete(contas:list, indice, path):
    contas.pop(indice)

    create(path, contas)