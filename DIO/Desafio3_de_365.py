# Crie um programa que receba uma lista de números digitados pelo usuário (separados por espaço) e mostre qual é o maior número encontrado.

input_str = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(int, input_str.split()))

maior = numeros[0]
for num in numeros:
     if num > maior:
         maior = num
print(f"O maior número da lista é: {maior}")