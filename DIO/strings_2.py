nome = "Ernesto"
idade = 36
profissao = "Moderador N2"
curso = "Sistemas de Informação"

dados = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "curso": curso
}

print("Nome: %s Idade: %d Profissão: %s Curso: %s" % (nome, idade, profissao, curso))
print("Nome: {} Idade: {} Profissão: {} Curso: {}".format(nome, idade, profissao, curso))
print("Nome: {0} Idade: {1} Profissão: {2} Curso: {3}".format(nome, idade, profissao, curso))
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Curso: {curso}".format(nome=nome, idade=idade, profissao=profissao, curso=curso))
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Curso: {curso}") 
print("Nome: {nome} \nIdade: {idade} \nProfissão: {profissao} \nCurso: {curso}".format(**dados))

eu = "Ernesto da Silva Santana"

print(eu[:: -1])  # exemplos de fatiamento de strings
print(eu[0])
print(eu[:7])
print(eu[8:])
print(eu[8:16])
print(eu[8:16:2])
print(eu[:])

print(f''' 
      Eu sou o {eu}, Expert em Moderação Nv.2,
      com experiência em Supervisão de operações, 
      Lider de treinamento e Monitor de qualidade.
      ''') #exemplo de string multilinha ou multiplas ou triplas

