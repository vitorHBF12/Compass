lista_a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for palavra in lista_a:
    lista_inversa = palavra[::-1]
    if lista_inversa == palavra:
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")
