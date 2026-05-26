# parametros especiais
# objetos de primeira classe

'''def somar(a, b):  # Função que soma dois números
    return a + b

def subtrair(a, b):  # Função que subtrai dois números
    return a - b

def exibir_resultado(a, b, funcao):  # Função que exibe o resultado da operação
    resultado = funcao(a, b)    # Chama a função passada como argumento
    print(f"O resultado é = {resultado}") # Exibe o resultado da operação

exibir_resultado(10, 5, somar) # Exibe o resultado da soma
exibir_resultado(10, 5, subtrair) # Exibe o resultado da subtração

op = somar # Atribui a função somar à variável op

print(op(10, 5)) # Exibe o resultado da soma
'''
# exemplo de uso de variáveis globais
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)
print(salario) # Exibe o novo salário
