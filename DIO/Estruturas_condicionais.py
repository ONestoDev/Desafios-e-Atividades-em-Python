# MAIOR_IDADE = 18
# IDADE_ESPECIAL = 16

# idade = int(input("Informe a sua idade: "))

# if idade >= MAIOR_IDADE:
  #  print("Você tem idade para dirigir.")
# elif idade == IDADE_ESPECIAL:
  #  print("Você pode começar a fazer apenas as aulas teoricas.")
# else:
  #  print("Você não tem idade para dirigir.") 

''' conta_normal = False
conta_universitaria = True
conta_especial = False

saldo = 2000
saque = 1500
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com Sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do Cheque Especial!")
    else:
        print("Saldo insuficiente! Saque não realizado!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com Sucesso!")
    else: 
        print("Saldo insuficiente! Saque não realizado!")
elif conta_especial:
    if saldo >= saque:
        print("Saque realizado com Sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do Cheque Especial!")
    else:
        print("Saldo insuficiente! Saque não realizado!")
'''       

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"
print (f"{status} ao realizar o saque!")
