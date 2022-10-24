from customPrints import *
from math import sqrt
from os import system

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[36m'
CLEANCOLOR = '\033[0;0m'

def customSum(numbers):
    return sum(numbers)

def customSubtract(numbers):
    if len(numbers) == 1: return numbers[0]
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    
    return result

def customDivide(num1, num2):
    if num2 == 0: return "Números não podem ser divididos por 0"
    return num1 / num2
    

def customMultiply(numbers):
    if len(numbers) == 1: return numbers[0]
    result = 1
    for number in numbers:
        result *= number
    
    return result

def wagesSum(numbers):
    return sum(numbers)

def takeNumbers(text):
    qtt = int(input(f"Digite a quantidade de números que serão {text}: "))
    numbers = []
    for i in range(1, qtt+1):
        numbers.append(int(input(f"Digite o {i}º número: ")))

    return numbers

def menu():
    headerPrint('== SEJA BEM-VINDO ==')
    tablePrint(f"{RED}FUNÇÕES{CLEANCOLOR}", True, True)
    tablePrint('Somar - 1')
    tablePrint('Subtrair - 2')
    tablePrint('Dividir - 3')
    tablePrint('Multiplicar - 4')
    tablePrint('Calculo avançado - 5')
    headerPrint()

def advancedMenu():

    system("cls")
    headerPrint('== CALCULADORA AVANÇADA ==')
    tablePrint(f"{RED}TUTORIAL{CLEANCOLOR}", True, True)
    tablePrint(F'{BLUE}Digite a formula desejada seguindo os exemplos:{CLEANCOLOR}', colored= True)
    tablePrint('Somar = 2 + 2')
    tablePrint('Subtrair = 2 - 2')
    tablePrint('Dividir = 2 / 2')
    tablePrint('Multiplicar = 2 * 2')
    tablePrint('Elevar = 2 ** 2')
    tablePrint('Raiz quadrada = sqrt(2)')
    tablePrint(f'{BLUE}Parenteses podem ser usados para indicar prioridade!{CLEANCOLOR}', colored= True)
    headerPrint()

def menu():
    headerPrint('== SEJA BEM-VINDO ==')
    tablePrint(f"{RED}FUNÇÕES{CLEANCOLOR}", True, True)
    tablePrint('Somar - 1')
    tablePrint('Subtrair - 2')
    tablePrint('Dividir - 3')
    tablePrint('Multiplicar - 4')
    tablePrint('Calculo avançado - 5')
    headerPrint()