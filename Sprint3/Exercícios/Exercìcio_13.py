lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def lista_multiplo(multiplo):
    return multiplo * multiplo


lista_multiplo2 = list(map(lista_multiplo, lista_1))
print(lista_multiplo2)
