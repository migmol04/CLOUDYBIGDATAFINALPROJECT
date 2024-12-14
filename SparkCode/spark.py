from pyspark.sql import SparkSession
import AveragePrice
import DataOrganization
import InvertedIndex
import FilterByNumber
import advanced_analysis

def run_spark_analysis(input_path, output_path, operation):
    # Inicializar SparkSession
    spark = SparkSession.builder.appName("Spark Analysis").getOrCreate()
    
    if operation == "average_price":
        AveragePrice.average_close_per_year(input_path, output_path)
    elif operation == "data_organization":
        DataOrganization.reorganize_data(input_path, output_path)
    elif operation == "inverted_index":
        InvertedIndex.inverted_index_max_close(input_path, output_path)
    elif operation == "advanced_analysis":
        advanced_analysis.advanced_analysis(input_path, output_path)
    elif operation == "filter_by_number":
        FilterByNumber.filter_by_number(input_path, output_path)
    else:
        print(f"Operación desconocida: {operation}")
        print("Operaciones disponibles: average_price, data_organization, inverted_index, advanced_analysis")
    
    # Detener SparkSession
    spark.stop()
