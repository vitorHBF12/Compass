def remove_duplicates(lista):
    return list(set(lista))


lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_nova = remove_duplicates(lista)
print(lista_nova)
