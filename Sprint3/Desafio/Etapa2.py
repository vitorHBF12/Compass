with open('actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    total_gross = 0
    num_filmes = 0

    for linha in linhas[1:]:
        colunas = linha.strip().split(',')

        if colunas[5] and colunas[5] != 'Gross':
            try:
                gross = float(colunas[5])

                total_gross += gross
                num_filmes += 1
            except ValueError:
                pass

    if num_filmes > 0:
        media_gross = total_gross / num_filmes
        print(f"A média é de {media_gross:.2f} milhões de dólares.")
