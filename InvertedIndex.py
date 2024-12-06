from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, max, collect_list, to_date

def inverted_index_max_close(input_path, output_path):
    spark = SparkSession.builder.appName("InvertedIndexMaxClose").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)
    df = df.withColumn("Date", to_date(col("Date"), "dd-MM-yyyy")) \
           .withColumn("Year", year(col("Date")))
    
    # Encontrar el valor máximo de Close por año
    max_close = df.groupBy("Year").agg(max("Close").alias("MaxClose"))
    
    # Relacionar las fechas con el valor máximo
    inverted_index = (
        df.join(max_close, (df["Year"] == max_close["Year"]) & (df["Close"] == max_close["MaxClose"]))
          .groupBy("Year", "MaxClose")
          .agg(collect_list("Date").alias("Dates"))
          .select("Year", "MaxClose", "Dates")
    )

    inverted_index.show()
    inverted_index.write.mode("overwrite").json(output_path)
    spark.stop()