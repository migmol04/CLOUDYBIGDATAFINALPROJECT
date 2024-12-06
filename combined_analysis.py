from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, year, to_date

def combined_analysis(input_path, output_path):
    spark = SparkSession.builder.appName("CombinedAnalysis").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)
    df = df.withColumn("Date", to_date(col("Date"), "dd-MM-yyyy")) \
           .withColumn("Year", year(col("Date")))

    # 1. Promedio anual de cierre
    avg_close = df.groupBy("Year").agg(avg("Close").alias("AvgClose"))

    # 2. Máximo y mínimo cierre por año
    max_min_close = df.groupBy("Year").agg(
        max("Close").alias("MaxClose"),
        min("Close").alias("MinClose")
    )

    # 3. Combinación de resultados
    combined_result = avg_close.join(max_min_close, on="Year")

    combined_result.show()
    combined_result.write.mode("overwrite").csv(output_path, header=True)
    spark.stop()