from controller import salvar, listar

def menu():
    print('*'*20, 'Menu', '*'*20)

    cond = 'sim'

    while cond == 'sim':
        salvar(input("Digite um nome: "))
        cond = input("Deseja continuar?\nsim\nnão\n:> ")

menu()
print("A lista de nomes inseridos\n", listar())