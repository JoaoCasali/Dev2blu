class Pessoa():
    def __init__(self, nome, sobrenome, idade, cpf) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        print(self)