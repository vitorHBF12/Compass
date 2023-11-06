
from pyspark.sql import SparkSession

# Configurando a sessão Spark com as configurações desejadas
spark = SparkSession.builder.appName("MyApp") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.driver.maxResultSize", "2g") \
    .getOrCreate()

# Inicialize a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Carregue o arquivo CSV em um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Mostre as primeiras 5 linhas
df_nomes.show(5)

# Renomeie a coluna para 'Nomes'
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Mostre o esquema
df_nomes.printSchema()

# Mostre 10 linhas do DataFrame
df_nomes.show(10)

# Adicione a coluna 'Escolaridade' com valores aleatórios
from pyspark.sql.functions import rand
escolaridade = df_nomes.select("Nomes", (rand() * 3).cast("int").alias("Escolaridade"))
df_nomes = df_nomes.join(escolaridade, on=["Nomes"])

# Adicione a coluna 'Pais' com nomes de países da América do Sul aleatórios
paises_sulamerica = ["Brasil", "Argentina", "Chile", "Colômbia", "Equador", "Uruguai", "Paraguai", "Venezuela", "Bolívia", "Peru", "Suriname", "Guiana", "Guiana Francesa"]
pais = df_nomes.select("Nomes", (rand() * len(paises_sulamerica)).cast("int").alias("Pais"))
df_nomes = df_nomes.join(pais, on=["Nomes"])

# Adicione a coluna 'AnoNascimento' com anos aleatórios entre 1945 e 2010
ano_nascimento = df_nomes.select("Nomes", (rand() * (2010 - 1945 + 1) + 1945).cast("int").alias("AnoNascimento"))
df_nomes = df_nomes.join(ano_nascimento, on=["Nomes"])

# Selecione pessoas que nasceram neste século
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)
df_select.show(10)

# Registre o DataFrame como uma tabela temporária para Spark SQL
df_nomes.createOrReplaceTempView("pessoas")

# Consulta SQL para selecionar pessoas que nasceram neste século
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show(10)

# Conte o número de pessoas da geração Millennials (1980-1994) usando o método select
millennials_count = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()
print(f"Número de Millennials no Dataset: {millennials_count}")

# Conte o número de pessoas da geração Millennials usando Spark SQL
millennials_count_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994").collect()[0][0]
print(f"Número de Millennials no Dataset (Spark SQL): {millennials_count_sql}")

# Consulta Spark SQL para obter a quantidade de pessoas por país e geração
query = """
SELECT Pais, 
       CASE 
           WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers' 
           WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X' 
           WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials' 
           WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z' 
       END AS Geração, 
       COUNT(*) AS Quantidade 
FROM pessoas
GROUP BY Pais, Geração
ORDER BY Pais, Geração
"""

df_pais_geracao_quantidade = spark.sql(query)
df_pais_geracao_quantidade.show()
