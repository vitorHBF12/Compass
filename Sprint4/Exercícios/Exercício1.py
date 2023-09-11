# Abrir o arquivo 'number.txt' em modo de leitura
with open('number.txt', 'r') as arquivo:
    # Ler todas as linhas do arquivo e mapear para inteiros
    numeros = map(int, arquivo.readlines())

    # Filtrar os números pares
    numeros_pares = filter(lambda x: x % 2 == 0, numeros)

    # Encontrar os 5 maiores números pares em ordem decrescente
    cinco_maiores_pares = sorted(numeros_pares, reverse=True)[:5]

    # Calcular a soma dos 5 maiores números pares
    soma = sum(cinco_maiores_pares)

# Imprimir os resultados
print(cinco_maiores_pares)
print(soma)
