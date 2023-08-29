with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    atores_receitas = []

    for linha in linhas[1:]:
        coluna_actor = linha.find(',')
        coluna_total_gross = linha.rfind(',')
        ator = linha[:coluna_actor].strip()
        receita_bruta_str = linha[coluna_total_gross +
                                  1:].replace(' ', '').replace(',', '')

        if receita_bruta_str:
            receita_bruta = float(receita_bruta_str)
            atores_receitas.append((ator, receita_bruta))

    atores_ordenados = sorted(
        atores_receitas, key=lambda item: item[1], reverse=True)

    for ator, receita_bruta in atores_ordenados:
        print(f"{ator} - {receita_bruta:.2f}")
