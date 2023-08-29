class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y


# Valores de teste
x = 4
y = 5

# Criando uma instância da classe Calculo
calculadora = Calculo()

# Realizando as operações e imprimindo os resultados
soma = calculadora.somar(x, y)
subtracao = calculadora.subtrair(x, y)

print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
