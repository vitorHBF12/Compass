with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    filmes_contagem = {}

    for linha in linhas[1:]:
        colunas = linha.strip().split(',')
        filme = colunas[4]
        filme = filme.strip()

        if filme in filmes_contagem:
            filmes_contagem[filme] += 1
        else:
            filmes_contagem[filme] = 1

    filmes_ordenados = sorted(filmes_contagem.items(),
                              key=lambda item: (-item[1], item[0]))

    for sequencia, (filme, quantidade) in enumerate(filmes_ordenados, start=1):
        print(f"{sequencia} - O filme {filme} aparece {quantidade} vezes")
