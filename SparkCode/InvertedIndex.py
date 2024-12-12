from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, max, collect_list, to_date, concat_ws

def inverted_index_max_close(input_path, output_path):
    spark = SparkSession.builder.appName("InvertedIndexMaxClose").getOrCreate()

    # Leer el archivo CSV de entrada
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Convertir la columna "Date" a formato de fecha y extraer el año
    df = df.withColumn("Date", to_date(col("Date"), "dd-MM-yyyy")) \
           .withColumn("Year", year(col("Date")))

    # Crear alias para el DataFrame original y el DataFrame de máximos
    df_alias = df.alias("df")
    max_close = df.groupBy("Year").agg(max("Close").alias("MaxClose")).alias("max_close")

    # Relacionar las fechas con el valor máximo usando los alias
    inverted_index = (
        df_alias.join(max_close, (df_alias["Year"] == max_close["Year"]) & (df_alias["Close"] == max_close["MaxClose"]))
          .groupBy(df_alias["Year"], max_close["MaxClose"])
          .agg(collect_list(df_alias["Date"]).alias("Dates"))
          .select(df_alias["Year"], max_close["MaxClose"], "Dates")
    )

    # Convertir la columna "Dates" de ARRAY<DATE> a STRING
    inverted_index = inverted_index.withColumn("Dates", concat_ws(", ", col("Dates")))

    # Guardar el resultado en formato CSV
    inverted_index.write.mode("overwrite").csv(output_path)

    # Detener SparkSession
    spark.stop()
