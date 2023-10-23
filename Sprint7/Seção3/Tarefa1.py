import pandas as pd
import numpy as np

# Passo 2: Ler o arquivo CSV
df = pd.read_csv('actors.csv')

# Pergunta 1: Identificar o ator/atriz com o maior número de filmes
actor_with_most_movies = df[df['Number of Movies']
                            == df['Number of Movies'].max()]
max_number_of_movies = actor_with_most_movies['Number of Movies'].values[0]
print(
    f"Ator/Atriz com o maior número de filmes: {actor_with_most_movies['Actor'].values[0]} ({max_number_of_movies} filmes)")

# Pergunta 2: Apresentar a média da coluna "Number of Movies"
average_number_of_movies = df['Number of Movies'].mean()
print(f"Média da coluna 'Number of Movies': {average_number_of_movies}")

# Pergunta 3: Apresentar o nome do ator/atriz com a maior média por filme
df['Average per Movie'] = df['Total Gross'] / df['Number of Movies']
actor_with_highest_average = df[df['Average per Movie']
                                == df['Average per Movie'].max()]
print(
    f"Ator/Atriz com a maior média por filme: {actor_with_highest_average['Actor'].values[0]}")

# Pergunta 4: Apresentar o(s) filme(s) mais frequente(s) e sua respectiva frequência
most_frequent_movies = df[df['Number of Movies']
                          == df['Number of Movies'].max()]
most_frequent_movie = most_frequent_movies['#1 Movie'].values[0]
frequency = most_frequent_movies.shape[0]
print(
    f"Filme(s) mais frequente(s): {most_frequent_movie} (Frequência: {frequency})")
