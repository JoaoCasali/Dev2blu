class Pessoa():

    def __init__(self, nome, sobrenome, idade, cpf) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__cpf = cpf

    def __str__(self) -> str:
        return f'{self.__nome} - {self.__sobrenome} - {self.__idade} - {self.__cpf}'

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome
    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
    
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf