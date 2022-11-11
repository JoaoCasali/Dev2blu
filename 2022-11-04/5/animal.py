class Animal():
    def __init__(self, especie, genero, idade, cor) -> None:
        self.especie = especie
        self.genero = genero
        self.idade = idade
        self.cor = cor
        print(self)