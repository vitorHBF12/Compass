class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada


crescente = Ordenadora([3, 4, 2, 1, 5])
resultado_crescente = crescente.ordenacaoCrescente()

decrescente = Ordenadora([9, 7, 6, 8])
resultado_decrescente = decrescente.ordenacaoDecrescente()

print(resultado_crescente)
print(resultado_decrescente)
