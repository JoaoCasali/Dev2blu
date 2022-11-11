from customPrints import *
from controller import *

system("cls")

while True:
    menu()
    option = input("Digite uma das opções descritas: ")

    match option:
        case '1':
            numbers = takeNumbers('somados')
            
            system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customSum(numbers)}')

        case '2':
            numbers = takeNumbers('subtraidos')
            
            system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customSubtract(numbers)}')

        case '3':
            number1 = int(input(f"Digite o 1º número: "))
            number2 = int(input(f"Digite o 2º número: "))
            
            system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customDivide(number1, number2)}')

        case '4':
            numbers = takeNumbers('multiplicados')
            
            system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customMultiply(numbers)}')

        case '5':
            advancedMenu()
            while True:
                try:
                    equation = eval(input("Digite a equação: "))
                    break
                except:
                    system("cls")
                    headerPrint()
                    tablePrint(f"{RED}EQUAÇÃO INVÁLIDA{CLEANCOLOR}", True, True)
                    headerPrint()

            system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {equation}')

        case _:
            headerPrint()
            tablePrint(f"{RED}OPÇÃO INVÁLIDA{CLEANCOLOR}", True, True)
            tablePrint()