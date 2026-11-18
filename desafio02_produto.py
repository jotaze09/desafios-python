"""Desafio final 02 - Uma pequena loja (atributos de classe, metodos e encapsulamento)."""


class Produto:
    taxa = 0.10  # atributo de classe: vale para todos os produtos

    def __init__(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O valor do produto nao pode ser negativo")
        self.valor = valor  # atributo de instancia

    def calcular_total(self) -> float:
        return round(self.valor * (1 + Produto.taxa), 2)

    @classmethod
    def definir_taxa(cls, nova_taxa: float) -> None:
        if nova_taxa < 0:
            raise ValueError("A taxa nao pode ser negativa")
        cls.taxa = nova_taxa


def main() -> None:
    p1 = Produto(100)
    p2 = Produto(200)

    print(p1.calcular_total())
    Produto.definir_taxa(0.15)
    print(p2.calcular_total())


if __name__ == "__main__":
    main()
