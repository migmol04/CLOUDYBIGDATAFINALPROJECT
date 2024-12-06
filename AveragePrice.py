from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, year

def average_close_per_year(input_path, output_path):
    spark = SparkSession.builder.appName("AverageClosePerYear").getOrCreate()
    
    # Leer el archivo CSV como DataFrame
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Calcular el promedio del precio de cierre por año
    average_close_per_year = (
        df.withColumn("Year", year(col("Date")))
          .groupBy("Year")
          .agg(avg("Close").alias("AverageClose"))
          .orderBy("Year")
    )

    #
    average_close_per_year.write.mode("overwrite").csv(output_path, header=True)

    # Detener la sesión de Spark
    spark.stop()
