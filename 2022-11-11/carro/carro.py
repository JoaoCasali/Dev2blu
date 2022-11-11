class Carro():
    def __init__(self, marca, modelo, valor) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__valor = valor

    def __str__(self) -> str:
        return f'{self.__marca} - {self.__modelo} - {self.__valor}'

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

