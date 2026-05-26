curso = "Python"
print(curso.strip())  # Remove espaços em branco no início e no fim
print(curso.lstrip()) # Remove espaços em branco no início
print(curso.rstrip()) # Remove espaços em branco no fim
print(curso.center(10, "#")) # Adiciona "#" para centralizar a string em um espaço de 10 caracteres
print(".".join(curso)) # Junta os caracteres da string com "."

carros = "gol" 
print(isinstance(carros, tuple))