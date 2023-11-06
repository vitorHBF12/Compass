import boto3
import pandas as pd
import requests
import json
import os

movie_info_list = []  # Inicialize a lista fora da função lambda_handler

def lambda_handler(event, context):
    # Nome do bucket S3 e caminho para o arquivo CSV
    s3 = boto3.client('s3')
    bucket_name = 'desafbucket'
    file_path = 'Raw/Local/CSV/Movies/2023/10/23/movies.csv'
    
    # Obter o objeto S3 sem baixar o arquivo localmente
    response = s3.get_object(Bucket=bucket_name, Key=file_path)
    
    # Converter os bytes em um DataFrame
    df = pd.read_csv(response['Body'], sep='|')
    mystery_movies = df[df['genero'].str.lower() == 'mystery']
    api_key = os.environ.get("chave")
    
    imdb_ids = set()  # Usar um conjunto para armazenar imdb_id únicos
    
    for imdb_id in mystery_movies['id']:
        if imdb_id not in imdb_ids:
            url = f'https://api.themoviedb.org/3/movie/{imdb_id}?api_key={api_key}'
            response = requests.get(url)
    
            if response.status_code == 200:
                movie_data = response.json()
                info = {
                    'imdb_id': movie_data.get('imdb_id', ''),
                    'popularity': movie_data.get('popularity', 0),
                    'production_countries': movie_data.get('production_countries', []),
                    'release_date': movie_data.get('release_date', ''),
                    'status': movie_data.get('status', ''),
                    'vote_average': movie_data.get('vote_average', 0),
                    'vote_count': movie_data.get('vote_count', 0),
                    'runtime': movie_data.get('runtime', 0),
                    'revenue': movie_data.get('revenue', 0)
                }
                movie_info_list.append(info)
                imdb_ids.add(imdb_id)  # Adicionar imdb_id ao conjunto
    
    # Criar um DataFrame com as informações desejadas
    movie_info_df = pd.DataFrame(movie_info_list)
    
    # Agora você tem um DataFrame com as informações desejadas
    print(movie_info_df)
    
    return {
        'statusCode': 200,
        'body': json.dumps("Processamento concluído.")
    }
