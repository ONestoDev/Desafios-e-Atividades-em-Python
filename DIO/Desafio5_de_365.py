# Crie um programa que receba um número inteiro N e mostre na tela uma pirâmide de asteriscos (*) com N linhas e depois inverter com as mesmas caracteristicas.

def piramide_asteriscos(n):
    for i in range(1, n + 1):
        espacos = ' ' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacos + asteriscos)
# Solicita ao usuário o número de linhas
num_linhas = int(input("Digite o número de linhas para a pirâmide: "))
piramide_asteriscos(num_linhas) 
print()  # Linha em branco para separar as duas pirâmides
# Imprime a pirâmide invertida
for i in range(num_linhas, 0, -1):
    espacos = ' ' * (num_linhas - i)
    asteriscos = '*' * (2 * i - 1)
    print(espacos + asteriscos) 


