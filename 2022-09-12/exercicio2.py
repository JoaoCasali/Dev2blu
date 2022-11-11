# exercício-02  usando a biblioteca interna random use o conceito de importação de toda biblioteca. crie quatro variáveis 
# recebendo valores, essas variáveis devem ser com tipos predefinidos tipo string, crie uma variável recebendo uma lista 
# das 4 variáveis, logo em seguida utilize importação da biblioteca e atribua a função embaralhar(shuffle). essa 
# importação irá realizar o embaralhamento dos valores recebidos atribua a lista a esta função. crie uma função de 
# impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. utilizando a 
# interpolação exiba em seguida com  a função de impressão a ordem definida dos nomes da variável lista.

import random

cor1 = str(input("Digite uma cor: "))
cor2 = str(input("Digite uma cor: "))
cor3 = str(input("Digite uma cor: "))
cor4 = str(input("Digite uma cor: "))

listaCores = [cor1, cor2, cor3, cor4]

print("-"*8, "Console", "-"*8)
print(f"Essa é a lista normal: {listaCores}")
random.shuffle(listaCores)
print(f"Essa é a lista embaralhada: {listaCores}")
