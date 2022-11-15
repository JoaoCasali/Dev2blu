from os import system
from time import sleep
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoasFisicas = []
pessoasJuridicas = []

while True:

    print("-- --".center(50, "="))
    print('1 - Cadastrar Pessoa Fisica\n2 - Cadastrar Pessoa Juridica\n3 - Listar Pessoas Fisicas\n4 - Listar Pessoas Jurididcas\n5 - Sair')
    opcao = input("=> ")
    match opcao:
        case '1':
            pessoasFisicas.append(
                PessoaFisica(
                    input("Digite o numero da conta: "), 
                    input("Digite a agencia: "), 
                    input("Digite o nome do titular: "), 
                    input("Digite o CPF: "), 
                    float(input("Digite o seu saldo atual: "))
                )
            )
            if input("Dejesa adicionar um segundo titular? (S/N)") == "S":
                pessoasFisicas[-1].segundo_titular = input("Digite o nome do segundo titular: ")

        case '2':
            pessoasJuridicas.append(
                PessoaJuridica(
                    input("Digite o numero da conta: "), 
                    input("Digite a agencia: "), 
                    input("Digite o nome do titular: "), 
                    input("Digite o CNPJ: "), 
                    float(input("Digite o seu saldo atual: "))
                )
            )
            if input("Dejesa adicionar um segundo titular? (S/N)") == "S":
                pessoasJuridicas[-1].segundo_titular = input("Digite o nome do segundo titular: ")

        case '3':
            system("cls")
            for pessoas in pessoasFisicas:
                print("-- --".center(50, "="))
                print(pessoas)
                sleep(1)

        case '4':
            system("cls")
            for pessoas in pessoasJuridicas:
                print("-- --".center(50, "="))
                print(pessoas)
                sleep(1)

        case '5':
            break
        case _:
            print("Opção inválida")
    