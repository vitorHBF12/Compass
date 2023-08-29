def print_parameters(*args, **kwargs):

    for arg in args:
        print(arg)

    for key, valor in kwargs.items():
        print(int(valor))


# Teste da função com os parâmetros fornecidos
print_parameters(1, 3, 4, 'hello', 'alguma coisa', x=20)
