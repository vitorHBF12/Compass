def soma_numeros_string(string_numeros):
    numeros = string_numeros.split(',')
    total = 0
    for num in numeros:
        # Converte cada número (string) para inteiro e soma ao total
        total += int(num)
    return total


string_de_numeros = "1,3,4,6,10,76"
soma = soma_numeros_string(string_de_numeros)
print("A soma dos valores é:", soma)
