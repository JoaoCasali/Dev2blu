class Animal():
    especie = ''
    cor = ''
    raca = ''
    def __str__(self) -> str:
        return f'{self.especie} - {self.cor} - {self.raca}'


