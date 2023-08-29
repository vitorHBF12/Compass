class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "Azul"
        self.capacidade = capacidade


# Criando os objetos da classe Avião com as entradas fornecidas
aviao1 = Aviao("BOIENG456", "1500 km/h", "400 passageiros")
aviao2 = Aviao("Embraer Praetor 600", "863 km/h", "14 passageiros")
aviao3 = Aviao("Antonov An-2", "258 km/h", "12 passageiros")

# Armazenando os objetos em uma lista
lista_avioes = [aviao1, aviao2, aviao3]

# Iterando pela lista e imprimindo os detalhes de cada avião
for aviao in lista_avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} e é da cor {aviao.cor}.")
