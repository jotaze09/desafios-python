"""Desafio final 01 - Crie um personagem (POO em Python)."""


class Personagem:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.vida = 100
        self.nivel = 1

    def receber_dano(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("O dano nao pode ser negativo")
        self.vida -= valor
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {valor} de dano. Vida restante: {self.vida}")

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def __str__(self) -> str:
        return f"{self.nome} | nivel {self.nivel} | vida {self.vida}"


def main() -> None:
    heroi = Personagem("Aria")
    vilao = Personagem("Gorak")

    heroi.receber_dano(30)
    vilao.receber_dano(80)

    print()
    print(heroi)
    print(vilao)
    print()
    print(f"{heroi.nome} esta vivo? {heroi.esta_vivo()}")
    print(f"{vilao.nome} esta vivo? {vilao.esta_vivo()}")


if __name__ == "__main__":
    main()

# Resposta da pergunta: cada personagem guarda a propria vida. O dano altera
# somente o objeto que recebeu, entao quem leva mais dano fica com menos vida
# (e quem chega a zero deixa de estar vivo).
