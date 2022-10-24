from controller import *
from os import system
from time import sleep

system("cls")

while True:
    menu()
    option = input("Digite uma das opções descritas: ")

    match option:
        case '1':  
            system("cls")
            headerPrint(f"== {GREEN}FICHA CADASTRAL{CLEANCOLOR} ==", True)
            name = str(input("Digite o nome do cliente: "))
            number = verifyNumber()
            cpf = verifyCPF()
            savePerson(
                {
                    'name': name,
                    'number': number,
                    'cpf': cpf
                }
            )

        case '2':
            system("cls")
            people = listPeople()
            headerPrint(f"== {GREEN}INDICE DE HOSPEDES{CLEANCOLOR} ==", True)
            for i, v in enumerate(people):
                tablePrint(f"{i + 1} - {v['name']}")
                maxIndex = i + 1  
            headerPrint()
            
            while True:
                try:
                    index = int(input("Digite um index existente: "))
                    break
                except:
                    tablePrint(f"{RED}DIGITE APENAS NÚMEROS{CLEANCOLOR}", True, True)

            if not(index < 0 or index > maxIndex): 
                delPerson(index)
            else:
                headerPrint()
                tablePrint(f"{RED}INDEX NÃO EXISTE{CLEANCOLOR}", True, True)
                headerPrint()

        case '3':            
            system("cls")
            people = listPeople()
            headerPrint(f"== {GREEN}LISTA DE HOSPEDES{CLEANCOLOR} ==", True)
            for person in people:
                tablePrint(f"Hospede: {person['name']}")
                tablePrint(f"Number: {person['number']}")
                tablePrint(f"CPF: {person['cpf']}")
                headerPrint()
                sleep(1)     

        case '4':
            
            system("cls")
            headerPrint(f"== {GREEN}PROCURAR HOSPEDE{CLEANCOLOR} ==", True)

            name = input("Digite o nome do hospede: ").lower().strip()
            system('cls')
            if not(findPerson(name)):
                headerPrint()
                tablePrint(f"{RED}PESSOA NÃO ENCONTRADA{CLEANCOLOR}", True, True)
                headerPrint()

        case '5':
            headerPrint()
            tablePrint(f"ATÉ MAIS", True)
            headerPrint()
            break

        case _:
            headerPrint()
            tablePrint(f"{RED}OPÇÃO INVÁLIDA{CLEANCOLOR}", True, True)
            tablePrint()