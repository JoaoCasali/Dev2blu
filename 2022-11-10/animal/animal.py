class Animal():

    def __init__(self, especie, raca, cor, porte) -> None:
        self.__especie = especie
        self.__raca = raca
        self.__cor = cor
        self.__porte = porte

    def __str__(self) -> str:
        return f'{self.__especie} - {self.__porte} - {self.__raca} - {self.__cor}'

    def GetEspecie(self):
        return self.__especie
    def SetEspecie(self, especie):
        self.__especie = especie

    def GetRaca(self):
        return self.__raca
    def SetRaca(self, raca):
        self.__raca = raca
    
    def GetCor(self):
        return self.__cor
    def SetCor(self, cor):
        self.__cor = cor

    def GetPorte(self):
        return self.__porte
    def SetPorte(self, porte):
        self.__porte = porte
