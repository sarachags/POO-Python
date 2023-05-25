class Ingresso():
    def __init__(self, valor):
        self.valor=valor

    def imprimeValor(self):
        print( f'{self.valor} está impresso...')

class Vip(Ingresso):
    def __init__(self, valor, ValorAdicional):
        super().__init__(valor)
        self.ValorAdicional=ValorAdicional
        

    def RetornoVip(self):
        self.valor+=self.ValorAdicional
        return self.valor


ingr = Vip(200,150)
print(vars(ingr))
print(ingr.RetornoVip())
print(vars(ingr))
