# Com base nas aulas passadas vamos criar um sorteio de lista e utilizando o conceito de estrutura de decisão exibir qual 
# foi a posição de ordem de inserção de dados que foi sorteada!  usando o conceito de importação otimizada importe a função 
# choice, logo em seguida crie quatro variáveis representadas por  nomes n1, n2, n3, n4, essas variáveis devem ser do tipo 
# string  e devem solicitar dados. crie uma variável que receba como lista estas quatro variáveis. crie uma variável usando a 
# importação otimizada e atribuindo a variável lista. crie uma função de impressão utilizando polimorfismo e quebra de linhas 
# para definir um cabeçalho para sua aplicação console. utilizando o conceito de interpolação exiba qual foi o nome sorteado. 
# utilizando o conceito de estrutura de decisão cria uma condição que exiba a ordem em que foi digitado o nome sorteado pela 
# variável de sorteio da lista!

from random import choice

n1 = input("Digite um nome: ")
n2 = input("Digite um nome: ")
n3 = input("Digite um nome: ")
n4 = input("Digite um nome: ")

listaNomes = [n1, n2, n3, n4]
print("-"*8, "Cabeçalho", "-"*8)

sorteado = choice(listaNomes)
print(f'O nome sorteado foi {sorteado}')

if listaNomes[0] == sorteado:
    print("Esse foi o primeiro nome da lista.")

elif listaNomes[1] == sorteado:
    print("Esse foi o segundo nome da lista.")

elif listaNomes[2] == sorteado:
    print("Esse foi o terceiro nome da lista.")

else:
    print("Esse foi o quarto nome da lista.")