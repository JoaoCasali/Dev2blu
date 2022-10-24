from customPrints import headerPrint, tablePrint
from datetime import datetime

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[36m'
CLEANCOLOR = '\033[0;0m'

CPFS = ["00000000000","11111111111", "22222222222", "33333333333", "44444444444", 
        "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]

def savePerson(person):
    with open('hotel/clientes.txt', 'a') as arq:
        arq.write(str(person)+ '\n')       

def listPeople():
    lista = []
    with open('hotel/clientes.txt', 'r') as arq:
        for n in arq:
            lista.append(eval(n))

    return lista

def delPerson(index):

    with open('hotel/clientes.txt', 'r') as arq:
        lines = arq.readlines()
    
    arqPointer = 1
    with open('hotel/clientes.txt', 'w') as fw:
        for line in lines:
            
            if arqPointer != index:
                fw.write(line)
            arqPointer += 1

def findPerson(name):

    people = listPeople()
    for person in people:
        if person['name'].lower() == name:
            headerPrint()
            tablePrint(f"Hospede: {person['name']}")
            tablePrint(f"Number: {person['number']}")
            tablePrint(f"CPF: {person['cpf']}")
            headerPrint()
            return True
    return False

def verifyCPF():
    while True:
        varcpf = input('Digite o CPF do cliente: ')

        hasError = False
        # Limpa o cpf, retira pontos traços e tudo que não seja um número
        cpf = [int(char) for char in varcpf if char.isdigit()]        

        # Verifica se o cpf são números repetidos
        if ''.join(map(str, cpf)) in CPFS:
            hasError = True

        # verifica se o tamanho está correto
        if len(cpf) != 11:
            hasError = True

        if not(hasError):
            for i in range(9, 11):
                value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
                digit = ((value * 10) % 11) % 10
                if digit != cpf[i]:
                    hasError = True
            
        if hasError:
            headerPrint()
            tablePrint(f"{RED}CPF inválido!!{CLEANCOLOR}", True, True)
            headerPrint()
        else:
            cpf = ''.join(map(str, cpf))
            return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def verifyNumber():
    while True:
        vartelefone = input('Telefone com DDD(47900000000): ')
        if not(vartelefone.isnumeric()) or len(vartelefone) != 11:
            headerPrint()
            tablePrint(f'{RED}NÚMERO INVÁLIDO!{CLEANCOLOR}', True, True)
            headerPrint()
        else:
            return f"({vartelefone[0:2]}) {vartelefone[2:7]}-{vartelefone[7:]}"

def menu():
    headerPrint('== SEJA BEM-VINDO ==')
    tablePrint(f"{BLUE}{greeting(datetime.now())}{CLEANCOLOR}", True, True)
    tablePrint(f"{RED}FUNÇÕES{CLEANCOLOR}", True, True)
    tablePrint('Fazer check-in - 1')
    tablePrint('Fazer check-out - 2')
    tablePrint('Listar hospedes - 3')
    tablePrint('Procurar hospedes - 4')
    tablePrint('Sair do programa - 5')
    headerPrint()

def greeting(date):
    date = int(date.strftime('%H'))
    if date < 12:
        return 'Bom dia'
    elif date > 12 and date < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite'

