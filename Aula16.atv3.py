class Forma:
    def __init__(self):
        self.area=0
        self.perimetro=0

class retangulo(Forma):
    def __init__(self):
        super().__init__()

    def CalcularArea(self,base,altura):
        self.base=base
        self.altura = altura
        self.area =self.base*self.altura
        print(f'A área do retângulo é {self.area}')

    def CalcularPerimetro(self,base,altura):
        self.base = base
        self.altura = altura
        self.perimetro = ((self.base*2) + (2*self.altura))
        print(f'A perimetro do retângulo é {self.area}')

    def __init__(self):
        super().__init__()

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def CalcularArea(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = (self.base * self.altura)/2
        print(f'A área do Triângulo é {self.area}')

    def CalcularPerimetro(self,base,altura):
        self.base = base
        self.altura = altura
        self.perimetro = 2*((base**2+altura**2)**(1/2))+base
        print(f'A perimetro do Triângulo é {self.area}')


forma1 = retangulo()
forma1.CalcularArea(5,5)
forma1.CalcularPerimetro(5,5)

forma2 = Triangulo()
forma2.CalcularArea(5,5)
forma2.CalcularPerimetro(5,5)