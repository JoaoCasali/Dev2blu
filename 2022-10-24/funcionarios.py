

def cadastrar():

    nome = input("Digite seu nome: ")
    idade = input("Digite sua data de nascimento: ")
    trabalho = input("Digite o numero da sua carteira de trabalho: ")

    if trabalho != '0':
        contratacao = input("Digite o ano de contratação do seu primeiro emprego: ")
        salario = float(input("Digite o salario: "))
    
        global funcionario
        funcionario = {
                'nome': nome,
                'idade': idade,
                'trabalho': trabalho,
                'contratacao': contratacao,
                'salario': salario
            }

cadastrar()

print(funcionario)
