class Imovel:
    def __init__(self, valor_base):
        self.valor_base = valor_base

    def calcular_aluguel(self):
        return self.valor_base


class Apartamento(Imovel):

    def __init__(self, quartos, garagem, possui_criancas):
        super().__init__(700)

        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):

        valor = self.valor_base

        if self.quartos == 2:
            valor += 200

        if self.garagem:
            valor += 300

        if not self.possui_criancas:
            valor *= 0.95

        return valor


class Casa(Imovel):

    def __init__(self, quartos, garagem):
        super().__init__(900)

        self.quartos = quartos
        self.garagem = garagem

    def calcular_aluguel(self):

        valor = self.valor_base

        if self.quartos == 2:
            valor += 250

        if self.garagem:
            valor += 300

        return valor


class Estudio(Imovel):

    def __init__(self, vagas):
        super().__init__(1200)

        self.vagas = vagas

    def calcular_aluguel(self):

        valor = self.valor_base

        if self.vagas >= 2:

            valor += 250

            vagas_extras = self.vagas - 2

            if vagas_extras > 0:
                valor += vagas_extras * 60

        return valor