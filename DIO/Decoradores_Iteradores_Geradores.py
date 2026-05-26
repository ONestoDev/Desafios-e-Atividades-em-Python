import time
import functools

def tempo_execucao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper
@tempo_execucao

def tarefa_pesada():
    time.sleep(2)
    print("Tarefa pesada concluída.")

tarefa_pesada()

def autenticar(func):
    def wrapper(*args, **kwargs):
        print("Autenticando usuário...")
        return func(*args, **kwargs)
    return wrapper

@autenticar
def acessar_dados_sensiveis():
    print("Acessando dados sensíveis...")

acessar_dados_sensiveis()

def contagemRegressiva(n):
    print("Iniciando contagem regressiva...")
    while n > 0:
        yield n
        n -= 1
    print("Contagem regressiva concluída!")
for i in contagemRegressiva(5):
    print(i)
