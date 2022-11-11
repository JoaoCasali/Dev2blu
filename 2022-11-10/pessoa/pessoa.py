class Pessoa():

    def __init__(self, nome, sobrenome, idade, cpf) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__cpf = cpf

    def __str__(self) -> str:
        return f'{self.__nome} - {self.__sobrenome} - {self.__idade} - {self.__cpf}'

    def GetNome(self):
        return self.__nome
    def SetNome(self, nome):
        self.__nome = nome

    def GetSobrenome(self):
        return self.__sobrenome
    def SetSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
    
    def GetIdade(self):
        return self.__idade
    def SetIdade(self, idade):
        self.__idade = idade

    def GetCpf(self):
        return self.__cpf
    def SetCpf(self, cpf):
        self.__cpf = cpf