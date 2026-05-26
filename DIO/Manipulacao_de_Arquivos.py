#file = open("C:\\Users\\Ernesto\\OneDrive\\Documentos\\Projetos Faculdade\\trilha-python-dio\\05 - Manipulação de arquivos\\lorem.txt", "r")
#print(file.read())
#file.close()

#arquivo = open(
#    "C:\\Users\\Ernesto\\OneDrive\\Documentos\\Projetos Faculdade\\DIO\\Python Developer - Suzano\\testes.txt", "w"
#)
#arquivo.write("Linha 1.")
#arquivo.writelines(["Python"])
#arquivo.close()

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1
#try:
#    with open(ROOT_PATH / "pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
#        escritor = csv.writer(arquivo)
#        escritor.writerow(["ID", "Nome"])
#        escritor.writerow(["01", "Ernesto"]) 
#        escritor.writerow(["02", "Maria"])
#except IOError as exc:
#    print(f"Erro ao manipular o arquivo: ", {exc})

try:
    with open(ROOT_PATH / "pessoas.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f"ID: {row["ID"]}")
            print(f"Nome: {row["Nome"]}")
except IOError as exc:
    print(f"Erro ao manipular o arquivo. {exc}")