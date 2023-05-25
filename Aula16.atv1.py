class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f' O {self.nome} foi comer...')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f' O {self.nome} foi latindo...')

    def comer(self, comida_cachorro):
        self.comida_cachorro=comida_cachorro
        print(f' O {self.nome} foi comer {self.comida_cachorro}')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f' O {self.nome} foi miando...')

    def comer(self, comida_gato):
        self.comida_gato=comida_gato
        print(f' O {self.nome} foi beber {self.comida_gato}')

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f' O {self.nome} foi pulando...')

dog = Cachorro("Cachorrinho", "Cinza")
cat = Gato("Gatinho", "Branco")
elho = Gato("Cenourinha", "Rosa")

print(vars(dog))
dog.comer("Ração")
print(vars(cat))
cat.comer("Leite")
print(vars(elho))