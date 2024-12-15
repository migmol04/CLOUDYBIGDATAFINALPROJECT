from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def filter_by_number(input_path, output_path):
    spark = SparkSession.builder.appName("FilterByMinClose").getOrCreate()
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    while True:
        try:
            min_close = float(input("Introduce el precio mínimo para filtrar los valores de 'Close': "))
            break
        except ValueError:
            pass

    df = df.withColumn("Date", to_date(col("Date"), "dd-MM-yyyy"))
    df = df.filter(df["Date"].isNotNull())

    average_close_per_year = (
        df.withColumn("Year", year(col("Date")))
          .groupBy("Year")
          .agg(avg("Close").alias("AverageClose"))
          .orderBy("Year")
    )
    
    filtered_df = average_close_per_year.filter(col("AverageClose") > 30)
    filtered_df.write.mode("overwrite").csv(output_path, header=True)

    spark.stop()
