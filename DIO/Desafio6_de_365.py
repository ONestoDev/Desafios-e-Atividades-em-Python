# Crie um programa que receba uma lista de números digitados pelo usuário (separados por espaço) e mostre qual é o maior, o menor e a media e por fim a mediana dos números.

input_str = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(int, input_str.split()))

maior = numeros[0]
menor = numeros[0]
soma = 0
for num in numeros:
     if num > maior:
         maior = num
     if num < menor:
         menor = num
     soma += num
media = soma / len(numeros)
print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")
print(f"A média dos números da lista é: {media}")

# Calculando a mediana
numeros.sort()
n = len(numeros)
if n % 2 == 1:
    mediana = numeros[n // 2]
else:
    mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
print(f"A mediana dos números da lista é: {mediana}")