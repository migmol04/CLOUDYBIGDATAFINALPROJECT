from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def filter_by_number(input_path, output_path):

    spark = SparkSession.builder.appName("FilterByMinClose").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)

    try:
        min_close = float(input("Introduce el precio mínimo para filtrar los valores de 'Close': "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        spark.stop()
        return

    filtered_df = df.filter(col("Close") > min_close)
    filtered_df.write.mode("overwrite").csv(output_path, header=True)

    spark.stop()
