with open('actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    max_media = 0
    ator_com_maior_media = ""

    for linha in linhas[1:]:
        colunas = linha.strip().split(',')
        ator = colunas[0]
        media = float(colunas[3])

        if media > max_media:
            max_media = media
            ator_com_maior_media = ator

    print(
        f"O ator/atriz com a maior média de receita  é {ator_com_maior_media}, com uma média de {max_media:.2f} milhões de dólares.")
