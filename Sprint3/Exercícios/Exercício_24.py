class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)


# Criando objetos e chamando os métodos de ordenação
crescente = Ordenadora([3, 4, 2, 1, 5])
crescente.ordenacaoCrescente()

decrescente = Ordenadora([9, 7, 6, 8])
decrescente.ordenacaoDecrescente()

# Imprimindo os resultados
print(crescente.listaBaguncada)
print(decrescente.listaBaguncada)
