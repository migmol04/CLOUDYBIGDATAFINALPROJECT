from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, row_number, sum, year, to_date
from pyspark.sql.window import Window

def advanced_analysis(input_path):
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

    # Extraer los años seleccionados
    top_years = [row["Year"] for row in ranked_years.collect()]

    # Filtrar datos solo para los años seleccionados
    filtered_df = df.filter(col("Year").isin(top_years))

    # Calcular la tendencia acumulativa de precios para cada año
    trend_analysis = (
        filtered_df.select("Year", "Date", "Close")
                   .orderBy("Year", "Date")
                   .withColumn("CumulativeClose", sum("Close").over(Window.partitionBy("Year").orderBy("Date")))
    )

    # Convertir resultados a pandas para graficar
    ranked_years_pd = ranked_years.toPandas()
    trend_analysis_pd = trend_analysis.toPandas()

    spark.stop()
    return ranked_years_pd, trend_analysis_pd
