import csv

# Função para calcular a média com duas casas decimais


def calcular_media(notas):
    return round(sum(notas) / len(notas), 2)


# Lê o arquivo CSV
with open('estudantes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Lista para armazenar os resultados
    resultados = []

    # Itera sobre as linhas do arquivo
    for row in reader:
        nome = row[0]
        notas = [int(nota) for nota in row[1:]]

        # Ordena as notas em ordem decrescente
        notas.sort(reverse=True)

        # Seleciona as três maiores notas
        tres_maiores_notas = notas[:3]

        # Calcula a média com duas casas decimais usando map
        media = list(map(lambda nota: round(nota, 2), tres_maiores_notas))

        # Formata a saída com round aplicado aos resultados
        resultado = f'Nome: {nome} Notas: {media} Média: {round(calcular_media(tres_maiores_notas), 2)}'

        # Adiciona o resultado à lista
        resultados.append(resultado)

    # Ordena os resultados em ordem alfabética pelo nome do estudante usando sorted
    resultados_ordenados = sorted(resultados)

    # Imprime os resultados ordenados
    for resultado in resultados_ordenados:
        print(resultado)
