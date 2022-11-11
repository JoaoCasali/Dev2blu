class Pessoa():
    nome = ''
    sobrenome = ''
    idade = 0
    cpf = ''
    def __str__(self) -> str:
        return f'{self.nome} - {self.sobrenome} - {self.idade} - {self.cpf}'


