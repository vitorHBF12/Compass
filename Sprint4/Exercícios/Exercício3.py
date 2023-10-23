from functools import reduce
lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]


def calcula_saldo(lancamentos) -> float:
    def mapear_para_valores(
        tupla): return tupla[0] if tupla[1] == 'C' else -tupla[0]

    valores = map(mapear_para_valores, lancamentos)

    saldo_final = reduce(lambda x, y: x + y, valores)

    return saldo_final


saldo_final = calcula_saldo(lancamentos)

print("Saldo final:", saldo_final)
