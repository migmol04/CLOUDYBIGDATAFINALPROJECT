from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, row_number, sum, year, to_date
from pyspark.sql.window import Window

def advanced_analysis(input_path, output_path):
    spark = SparkSession.builder.appName("AdvancedAnalysisForGraphs").getOrCreate()

    # Leer y preparar el dataset
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    df = df.withColumn("Date", to_date(col("Date"), "dd-MM-yyyy")) \
           .withColumn("Year", year(col("Date")))

    # Calcular estadísticas anuales
    annual_stats = (
        df.groupBy("Year")
          .agg(
              avg("Close").alias("AvgClose"),
              max("Close").alias("MaxClose"),
              min("Close").alias("MinClose")
          )
    )

    # Rankeo de los años por promedio de cierre
    window_spec = Window.orderBy(col("AvgClose").desc())
    ranked_years = (
        annual_stats.withColumn("Rank", row_number().over(window_spec))
                    .filter(col("Rank") <= 3)  # Seleccionar los 3 años con mayor promedio
    )

    # Guardar ranked_years en un archivo CSV
    ranked_years.write.mode("overwrite").option("header", "true").csv(f"{output_path}/ranked_years")

    # Filtrar datos solo para los años seleccionados
    top_years = [row["Year"] for row in ranked_years.collect()]
    filtered_df = df.filter(col("Year").isin(top_years))

    # Calcular la tendencia acumulativa de precios para cada año
    trend_analysis = (
        filtered_df.select("Year", "Date", "Close")
                   .orderBy("Year", "Date")
                   .withColumn("CumulativeClose", sum("Close").over(Window.partitionBy("Year").orderBy("Date")))
    )

    # Guardar trend_analysis en un archivo CSV
    trend_analysis.write.mode("overwrite").option("header", "true").csv(f"{output_path}/trend_analysis")

    # Detener la sesión de Spark
    spark.stop()

