lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def my_map(multiplo):
    return multiplo * multiplo


lista_multiplo2 = list(map(my_map, lista_1))
print(lista_multiplo2)
