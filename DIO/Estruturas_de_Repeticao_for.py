texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um interável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
    
print() # adiciona uma quebra de linha

for numero in range(0, 91, 9):
    print(numero, end=" ")
