import math

numero = int(input("Informe um número inteiro qualquer: "))
print("O dobro de {} é {}.".format(numero, numero * 2))
print("O Triplo de {} é {}.".format(numero, numero * 3))
print("A raiz quadrada de {} é {:.2f}.".format(numero, math.sqrt(numero))) ##para calcular a raiz quadrada sem importar a biblioteca math é = numero ** (1/2)