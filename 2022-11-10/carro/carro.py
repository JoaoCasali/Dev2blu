class Carro():
    def __init__(self, marca, modelo, valor) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__valor = valor

    def __str__(self) -> str:
        return f'{self.__marca} - {self.__modelo} - {self.__valor}'

    def GetMarca(self):
        return self.__marca
    def SetMarca(self, marca):
        self.__marca = marca

    def GetModelo(self):
        return self.__modelo
    def SetModelo(self, modelo):
        self.__modelo = modelo
    
    def GetValor(self):
        return self.__valor
    def SetValor(self, valor):
        self.__valor = valor

