nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
genero = bool(int(input("Insira seu genero (Masculino = 1, Feminino = 0): ")))

print("Seu nome é: {}|Seu sobrenome é: {}|Sua idade é: {}|Seu salário é: {}|Você é do sexo masculino: {}".format(nome, sobrenome, idade, salario, genero))