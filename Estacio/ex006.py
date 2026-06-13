import random

def advinha_numero():
    numeroSecreto = random.randint(0, 10)
    tentativas = 0

    print("Pensei em um número entre 0 e 10. Tente adivinhar...")

    while True:
        palpite = int(input("Seu palpite: "))
        tentativas += 1

        if palpite < numeroSecreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numeroSecreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você adivinhou o número {numeroSecreto} em {tentativas} tentativas.")
            break

advinha_numero()