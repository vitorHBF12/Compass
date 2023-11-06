# Passo 1: Instalar a biblioteca 'names'
# Certifique-se de que você já instalou a biblioteca 'names' com o comando 'pip install names'.

# Passo 2: Importar as bibliotecas
import random
import time
import os
import names

# Passo 3: Definir os parâmetros
random.seed(40)  # Define a semente de aleatoriedade

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Passo 4: Gerar nomes aleatórios
aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Passo 5: Gerar um arquivo de texto com os nomes
with open("nomes_aleatorios.txt", "w") as arquivo:
    for nome in dados:
        arquivo.write(nome + "\n")

print("Arquivo 'nomes_aleatorios.txt' criado com sucesso.")

# Passo 6: Abra o arquivo e verifique seu conteúdo em um editor de texto.
# Você pode abrir o arquivo 'nomes_aleatorios.txt' em qualquer editor de texto de sua preferência para verificar o conteúdo.
