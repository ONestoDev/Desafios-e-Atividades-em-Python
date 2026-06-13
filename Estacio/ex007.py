import math


def menu():
    print("\nEscolha uma opção:")
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Fatorial primeiro número")
    print("[ 5 ] Fatorial segundo número")
    print("[ 6 ] Novos numeros")
    print("[ 7 ] Sair")

def adicao(a, b):
    return a+b
def multiplicar(a, b):
    return a*b
def maior(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "São iguais"

def fatorial(n):
    return math.factorial(int(n))

def main():
    a = int(input("Informe o primeiro numero: "))
    b = int(input("Informe o segundo numero: "))

    while True:
        menu()
        opcao = int(input("Escolha uma opção (1-7): "))

        if opcao == 1:
            print(f"A soma de {a} e {b} é: {adicao(a, b)}")
        elif opcao == 2:
            print(f"A multiplicação de {a} e {b} é: {multiplicar(a, b)}")
        elif opcao == 3:
            print(f"O maior entre {a} e {b} é: {maior(a, b)}")
        elif opcao == 4:
            print(f"Fatorial do primeiro numero: {fatorial(a)}")
        elif opcao == 5:
            print(f"Fatorial do segundo numero: {fatorial(b)}")
        elif opcao == 6:
            a = int(input("Informe o primeiro numero: "))
            b = int(input("Informe o segundo numero: "))
        elif opcao == 7:
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 7.")

main()