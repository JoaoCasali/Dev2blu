# exercício-01 usando a biblioteca interna random use o conceito de importação otimizada de (Escolha (Choice)) de lista , 
# crie quatro variáveis recebendo valores, essas variáveis devem ser com tipos predefinidos tipo cor, crie uma variável
# recebendo uma lista das 4 variáveis, logo em seguida crie outra variável recebendo a importação , essa importação irá 
# realizar o sorteio de um valor recebido. crie uma função de impressão utilizando polimorfismo e quebra de linhas para 
# definir um cabeçalho para sua aplicação console. utilizando a interpolação exiba em seguida com a função de impressão o 
# nome sorteado pela biblioteca random.

from random import choice

cor1 = str(input("Digite uma cor: "))
cor2 = str(input("Digite uma cor: "))
cor3 = str(input("Digite uma cor: "))
cor4 = str(input("Digite uma cor: "))

listaCores = [cor1, cor2, cor3, cor4]
print("-"*8, "Console", "-"*8)

print(f"A cor sorteada foi {choice(listaCores)}")