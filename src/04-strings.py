from string import Template

# combinar strings
cor = "Azul"
print("Carro " + cor)

# Formatação de string
cor = "Verde"
print("Carro %s" % cor)

# Formatação de string outro estilo
cor = "Laranja"
print("Carro {}".format(cor))

# Interpolação String f-String (Python 3.6+)
cor = "Laranja"
print(f"Carro {cor}")

# Usando Template
template = Template("Hello World, $lang")
print(template.substitute(lang="Python"))

# length
base = "Teste"
print(len(base))

# split
base = "Mesa Cadeira Computador Notebook Tablet Mouse Teclado"
print(base.split(' '))

# Strip
print(base.strip('MesaTeclado'))

# Index of
print(base.index('Cadeira'))

# Slicing
print(base[0:4])  # de x para y
print(base[:4])  # Do começo para y
print(base[5:])  # x do final para o começo

# Posição -5 do final para o começo
# Posição -2 do final para o começo
print(base[-7:-2])

# Maiúsculas
print(base.upper())

# Minúsculas
print(base.lower())

# Remover espaço do inicio ou fim
print(" Olá mundo  ".strip())

# Substituir String
print("Olá mundo".replace("mundo", "programador"))

# Dividir String
print("Olá-mundo".split('-'))
