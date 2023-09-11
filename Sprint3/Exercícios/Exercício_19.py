import random

random_list = random.sample(range(500), 50)
valor_minimo = min(random_list)
valor_maximo = max(random_list)
soma_valores = sum(random_list)
media = soma_valores / len(random_list)

random_list.sort()
tamanho_lista = len(random_list)
if tamanho_lista % 2 == 0:
    meio1 = random_list[tamanho_lista // 2 - 1]
    meio2 = random_list[tamanho_lista // 2]
    mediana = (meio1 + meio2) / 2
else:
    mediana = random_list[tamanho_lista // 2]

print(f"Média: {media:.2f}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
