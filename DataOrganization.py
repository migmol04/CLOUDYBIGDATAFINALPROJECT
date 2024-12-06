from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, avg, min, max, to_date

def reorganize_data(input_path, output_path):
    spark = SparkSession.builder.appName("DataOrganization").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)
    df = df.withColumn("Date", to_date(col("Date"), "dd-MM-yyyy")) \
           .withColumn("Year", year(col("Date")))

    # Calcular estadísticas anuales
    annual_stats = (
        df.groupBy("Year")
          .agg(
              avg("Close").alias("AvgClose"),
              min("Close").alias("MinClose"),
              max("Close").alias("MaxClose"),
              avg("Volume").alias("AvgVolume")
          )
    )
    annual_stats.write.mode("overwrite").csv(output_path, header=True)
    spark.stop()

# Usar la función
reorganize_data("ruta/a/tu/dataset.csv", "ruta/a/salida")
