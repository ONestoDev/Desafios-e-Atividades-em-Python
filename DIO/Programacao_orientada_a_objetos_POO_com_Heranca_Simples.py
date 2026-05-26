# Primeiro programa POO
'''João tem uma bicicletaria e gostaria de registrar as vendas de bicicletas.
Criaremos um programa onde João informe: cor, modelo, ano e valor da bicicleta.
uma bicicleta pode buzinar, parar e correr. Vamos adicioar esses comportamentos!(feito em 03/09/2025)'''
'''agora vamos adicionar o método especial __str__ para melhorar a apresentação do objeto (att 04/09/2025)'''

class Veiculo:
    def __init__(self, cor, placa, modelo, ano, valor):
        self.cor = cor
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def ligar_motor(self):
        print("O motor está ligado!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"    

class Motocicleta(Veiculo):
   pass
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    def __init__(self, cor, placa, modelo, ano, valor, carregado):
        super().__init__(cor, placa, modelo, ano, valor)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!")


moto = Motocicleta("Vermelha", "ABC-1234", "Honda CG 160", 2020, 15000)
moto.ligar_motor()
print(f"A moto é da marca {moto.modelo}, na cor {moto.cor} e custa R$ {moto.valor}")
carro = Carro("Preto", "DEF-5678", "Toyota Corolla", 2021, 120000)
carro.ligar_motor()
print(f"O carro é da marca {carro.modelo}, na cor {carro.cor} e custa R$ {carro.valor}")
caminhao = Caminhao("Branco", "GHI-9012", "Volvo FH", 2019, 300000, True)
caminhao.ligar_motor()
print(f"O caminhão é da marca {caminhao.modelo}, na cor {caminhao.cor} e custa R$ {caminhao.valor}, E ele está carregado?")
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)