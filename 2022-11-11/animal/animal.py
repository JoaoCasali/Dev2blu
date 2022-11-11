class Animal():

    def __init__(self, especie, raca, cor, porte) -> None:
        self.__especie = especie
        self.__raca = raca
        self.__cor = cor
        self.__porte = porte

    def __str__(self) -> str:
        return f'{self.__especie} - {self.__porte} - {self.__raca} - {self.__cor}'

    @property
    def especie(self):
        return self.__especie
    @especie.setter
    def especie(self, especie):
        self.__especie = especie
    
    @property
    def raca(self):
        return self.__raca
    @raca.setter
    def raca(self, raca):
        self.__raca = raca
    
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def porte(self):
        return self.__porte
    @porte.setter
    def porte(self, porte):
        self.__porte = porte
