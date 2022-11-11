# Com base nas aulas passadas vamos criar uma calculadora utilizando o conceito de estrutura de decisão. crie duas variáveis 
# recebendo dados numéricos com casas decimais, a descrição deve ser relacionada com primeira nota e segunda nota!
# crie uma variável para realizar este cálculo, não esqueça de utilizar o conceito de ordem de procedência aritmética.
# crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação 
# console. utilizando máscara de substituição  imprima de forma descritiva a primeira nota, utilize quebra de linha, 
# imprima a segunda nota, utilize a quebra de linha e imprima o resultado. Usando estrutura de decisão crie uma condição 
# onde o resultado for maior que sete imprima na sua aplicação console que este aluno está acima da média. Usando estrutura
# de decisão crie uma condição onde o resultado for igual a sete imprima na sua aplicação console que este aluno está na 
# média. Usando estrutura de decisão crie uma condição onde o resultado for entre cinco e sete imprima na sua aplicação 
# console que este aluno pode solicitar  recuperação. Usando estrutura de decisão crie uma condição onde o resultado for 
# entre quatro e cinco imprima na sua aplicação console que este aluno deve procurar o professor. Usando estrutura de 
# decisão crie uma condição de saída e imprima na sua aplicação console que este aluno infelizmente não atingiu o esperado!

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("-"*8, "Calculadora", "-"*8)
print("A primeira nota é: {}\nA segunda nota é: {}\nA média é: {}".format(nota1, nota2, media))

if media > 7.0:
    print("Você está acima da média!")

elif media == 7.0: 
    print("Você está na média!")

elif media > 5.0 < 7.0: 
    print("Você pode solicitar a recuperação!")

elif media >= 4.0 == 5.0: 
    print("Você deve procurar o professor!")

else:
    print("Você não atingiu o esperado!")