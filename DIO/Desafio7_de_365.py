# criar um programa que receba um numero inteiro e informe como ele é em binário.

numero = int(input("Digite um número inteiro: "))
binario = bin(numero)[2:]
print(f"O número {numero} em binário é: {binario}")


