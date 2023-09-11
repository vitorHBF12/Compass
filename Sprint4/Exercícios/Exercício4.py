def calcular_valor_maximo(operadores, operandos):
    resultados_compreensao = [eval(f"{a} {op} {b}")
                              for op, (a, b) in zip(operadores, operandos)]

    def calcular(op, valores):
        a, b = valores
        return eval(f"{a} {op} {b}")

    resultados_map = list(map(calcular, operadores, operandos))

    maior_valor = max(resultados_compreensao + resultados_map)
    return maior_valor


# Exemplo de uso
operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

maior = calcular_valor_maximo(operadores, operandos)
print(maior)
