from os import system
from time import sleep
from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.controller import create, read, update, delete

PATH_PESSOA_FISICA = "Banco/PessoaFisica.txt"
PATH_PESSOA_JURIDICA = "Banco/PessoaJuridica.txt"

def menu():
    lista_fisica = []
    lista_juridica = []
    while(True):
        lista_fisica = read(PATH_PESSOA_FISICA, PessoaFisica)
        lista_juridica = read(PATH_PESSOA_JURIDICA, PessoaJuridica)

        print("="*30, "Menu Principal", "="*30)
        print("1.Pessoa Fisica \n2.Pessoa Juridica \n")
        menu_inical = int(input("Digite o Tipo:> "))
        
        match menu_inical:
            case 1:
                menu = int(input("1.Criar PessoaFisica: \n2.Listar PessoasFisicas: \n3.Atualizar:\n4.Deletar: \nR:> "))
                match menu:
                    case 1:
                        pessoafisica = PessoaFisica(
                            str(input("Digite o Nome do 1° titular:> ")).strip(),
                            str(input("Digite o Cpf:> ")),
                            float(input("Digite o Saldo Inicial:> "))
                        )

                        print("Deseja Cadastrar um Segundo Titular:> \n")
                        v=str(input('Sim ou Não:> '))
                        if v=='Sim':
                            pessoafisica.segundo_titular = str(input("Digite o Nome do 2° Titular:> "))
                        
                        lista_fisica.append(pessoafisica)
                        create(PATH_PESSOA_FISICA, lista_fisica)

                    case 2:
                        system("cls")
                        for pessoa in lista_fisica:
                            print(f'Agencia: {pessoa.agencia}\nNumero da agencia: {pessoa.numero_agencia}\nTitular: {pessoa.titular}\nCPF: {pessoa.cpf}\nSegundo titular: {pessoa.segundo_titular}')
                            sleep(1)
                            print("-----------")

                    case 3:
                        nome = input("Digite o nome do titular que será atualizado: ").strip()
                        for pessoa in lista_fisica:
                            if pessoa.titular == nome:
                                update(lista_fisica, lista_fisica.index(pessoa), PessoaFisica, PATH_PESSOA_FISICA)

                    case 4:
                        nome = input("Digite o nome do titular que será deletado: ").strip()
                        for pessoa in lista_fisica:
                            if pessoa.titular == nome:
                                delete(lista_fisica, lista_fisica.index(pessoa), PATH_PESSOA_FISICA)
            case 2:
                menu = int(input("1.Criar PessoaJuridica: \n2.Listar PessoasJuridias: \n3.Atualizar:\n4.Deletar: \nR:> "))
                match menu:
                    case 1:
                        pessoajuridica = PessoaJuridica(
                            str(input("Digite o Nome do 1° titular:> ")).strip(),
                            str(input("Digite o CNPJ:> ")),
                            float(input("Digite o Saldo Inicial:> "))
                        )

                        print("Deseja Cadastrar um Segundo Titular:> \n")
                        v=str(input('Sim ou Não:> '))
                        if v=='Sim':
                            pessoajuridica.segundo_titular = str(input("digite o nome do 2° titular: "))
                        
                        lista_juridica.append(pessoajuridica)
                        create(PATH_PESSOA_JURIDICA, lista_juridica)

                    case 2:
                        system("cls")
                        for pessoa in lista_juridica:
                            print(f'Agencia: {pessoa.agencia}\nNumero da agencia: {pessoa.numero_agencia}\nTitular: {pessoa.titular}\nCNPJ: {pessoa.cnpj}\nSaldo Inicial: {pessoa.saldo_inicial}\nSegundo titular: {pessoa.segundo_titular}')
                            sleep(1)
                            print("-----------")
            
                    case 3:
                        nome = input("Digite o nome do titular que será atualizado: ").strip()
                        for pessoa in lista_fisica:
                            if pessoa.titular == nome:
                                update(lista_fisica, lista_fisica.index(pessoa), PessoaJuridica, PATH_PESSOA_JURIDICA)

                    case 4:
                        nome = input("Digite o nome do titular que será deletado: ").strip()
                        for pessoa in lista_fisica:
                            if pessoa.titular == nome:
                                delete(lista_fisica, lista_fisica.index(pessoa), PATH_PESSOA_JURIDICA)
    
            case _:
                break