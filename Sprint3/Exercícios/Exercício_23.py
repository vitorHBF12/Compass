class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y


x = 4
y = 5

calculadora = Calculo()
soma = calculadora.somar(x, y)
subtracao = calculadora.subtrair(x, y)

print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
