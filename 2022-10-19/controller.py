def salvar(nome):
    arq = open('19-10-2022/pessoas.txt', 'a')
    arq.write(nome + "\n")
    arq.close()

def listar():
    lista = []
    with open('19-10-2022/pessoas.txt', 'r') as arq:
        for n in arq:
            lista.append(n.strip())

        arq.close()
    return lista