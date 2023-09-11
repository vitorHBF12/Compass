def print_parameters(*args, **kwargs):

    for arg in args:
        print(arg)

    for chave, valor in kwargs.items():
        print(int(valor))


print_parameters(1, 3, 4, 'hello', 'alguma coisa', x=20)
