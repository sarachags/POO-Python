class Animal():
    def __init__(self, nome , cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print( f' O {self.nome} foi comer...')
    

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__( nome, cor)
    def latir(self):
        print( f' O {self.nome} foi latindo...')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__( nome, cor)
    def miar(self):
        print( f' O {self.nome} foi miando...')
    

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__( nome, cor)
    def pular(self):
        print( f' O {self.nome} foi pulando...')
    

dog = Cachorro("Bob", "Cinza")
cat = Gato("Leite", "Branco")
elho = Gato("Cenourinha", "Rosa")

print(vars(dog))

print(vars(cat))

print(vars(elho))