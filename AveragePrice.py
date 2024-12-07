from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, year, to_date

def average_close_per_year(input_path, output_path):
    spark = SparkSession.builder.appName("AverageClosePerYear").getOrCreate()
    
    # Leer el archivo CSV como DataFrame
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Convertir la columna 'Date' al tipo fecha con el formato 'DD-MM-YYYY'
    df = df.withColumn("Date", to_date(col("Date"), "dd-MM-yyyy"))

    # Filtrar filas donde 'Date' no sea nulo
    df = df.filter(df["Date"].isNotNull())

    # Calcular el promedio del precio de cierre por año
    average_close_per_year = (
        df.withColumn("Year", year(col("Date")))
          .groupBy("Year")
          .agg(avg("Close").alias("AverageClose"))
          .orderBy("Year")
    )

    # Mostrar el resultado para depurar
    average_close_per_year.show()

    # Guardar el resultado en el directorio de salida
    average_close_per_year.write.mode("overwrite").csv(output_path, header=True)

    # Detener la sesión de Spark
    spark.stop()
