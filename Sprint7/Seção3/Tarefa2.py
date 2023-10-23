##import org.apache.spark.sql.SparkSession
##import org.apache.spark.sql.functions._

# val spark = SparkSession.builder().appName("Contagem de Palavras no README").getOrCreate()

# val df = spark.read.text("file:/home/jovyan/README.md")

# val words = df.select(explode(split(col("value"), "\\s+")).alias("word"))

# val wordCounts = words.groupBy("word").count().orderBy(desc("count"))

# wordCounts.show()
