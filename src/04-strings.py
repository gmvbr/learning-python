from string import Template

# Juntar strings
cor = "Azul"
corDoCarro = "Carro " + cor
print(corDoCarro)

# Formatação de string
cor = "Verde"
corDoCarro = "Carro %s" % cor
print(corDoCarro)

# Formatação de string outro estilo
cor = "Laranja"
corDoCarro = "Carro {}".format(cor)
print(corDoCarro)

# Interpolação String f-String (Python 3.6)
cor = "Laranja"
corDoCarro = f"Carro {cor}"
print(corDoCarro)

# Usando Template
helloTemplate = Template("Hello World, $lang")
hello = helloTemplate.substitute(lang="Python")
print(hello)

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
