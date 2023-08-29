with open('actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    maximo_filmes = 0
    ator_com_mais_filmes = ""

    for linha in linhas[1:]:
        colunas = linha.strip().split(',')
        ator = colunas[0]
        num_filmes = int(colunas[2].replace(' ', '').replace('.', ''))

        if num_filmes > maximo_filmes:
            maximo_filmes = num_filmes
            ator_com_mais_filmes = ator

    print(
        f"O ator/atriz com o maior número de filmes é {ator_com_mais_filmes}, com um total de {maximo_filmes} filmes.")
