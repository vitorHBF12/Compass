# Abrir o arquivo actors.csv para leitura
with open('actors.csv', 'r') as arquivo:
    # Ler as linhas do arquivo
    linhas = arquivo.readlines()

    # Inicializar variáveis para acompanhar o ator com a maior média
    max_media = 0
    ator_com_maior_media = ""

    # Iterar pelas linhas, começando da segunda linha para ignorar o cabeçalho
    for linha in linhas[1:]:
        # Dividir a linha em colunas com base na vírgula
        colunas = linha.strip().split(',')

        # Extrair o nome do ator e a média por filme
        ator = colunas[0]
        media = float(colunas[3])

        # Verificar se a média é maior do que a máxima atual
        if media > max_media:
            max_media = media
            ator_com_maior_media = ator

    # Imprimir o resultado
    print(
        f"O ator/atriz com a maior média de receita  é {ator_com_maior_media}, com uma média de {max_media:.2f} milhões de dólares.")
