
class Animal:
    def __init__(self, especie, nro_patas, cor, sexo):
        self.especie = especie
        self.nro_patas = nro_patas
        self.cor = cor
        self.sexo = sexo

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, **kw):
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
            self.cor_bico = cor_bico
            super().__init__(**kw)

class Onitorrinco(Ave, Mamifero):
    pass
class Gato(Mamifero):
    pass
class Cachorro(Mamifero):
    pass   
class Leao(Mamifero):
    pass

gato = Gato(especie="Felis catus", nro_patas=4, cor="Preto", sexo="Macho")
print(f"O gato é da espécie {gato.especie}, tem {gato.nro_patas} patas e é da cor {gato.cor}")
print(gato)
onitorrinco = Onitorrinco(cor_bico="Laranja", especie="Ornithorhynchus anatinus", nro_patas=4, cor="Marrom", sexo="Macho")
print(onitorrinco)

