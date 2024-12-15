import os
import sys
import spark
from time import time 

def main():
    # Verificar los argumentos
    if len(sys.argv) < 4:
        print("Uso: python main.py <input_path> <output_path> <operation>")
        print("Operaciones disponibles: average_price, data_organization, inverted_index, advanced_analysis, filter_by_number")
        sys.exit(1)

    # Obtener rutas y operación desde los argumentos
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    operation = sys.argv[3]

    # Crear directorios si no existen
    os.makedirs(output_path, exist_ok=True)

    # Medir el tiempo de ejecución
    t_0 = time()

    # Llamar a la función de Spark con la operación seleccionada
    spark.run_spark_analysis(input_path, output_path, operation)

    # Calcular y mostrar el tiempo transcurrido
    elapsed_time = time() - t_0
    print(f"Tiempo transcurrido para la operación '{operation}': {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()
