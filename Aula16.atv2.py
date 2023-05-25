class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f'{self.valor} está impresso...')
        self.ValorAdicional = ValorAdicional


class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeValor(self, ValorAdicional):
        self.ValorAdicional=ValorAdicional
        self.valor += self.ValorAdicional
        return self.valor

ingr = Vip(200)
print(ingr.imprimeValor(40))
print(vars(ingr))