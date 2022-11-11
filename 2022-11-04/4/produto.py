class Produto():
    def __init__(self, id, NomeProduto, valor, quantidade) -> None:
        self.id = id
        self.NomeProduto = NomeProduto
        self.valor = valor
        self.quantidade = quantidade
        print(self)