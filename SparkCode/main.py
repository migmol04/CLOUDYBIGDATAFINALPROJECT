import os
import sys
import spark  

def main():
    # Verificar los argumentos
    if len(sys.argv) < 4:
        print("Uso: python main.py <input_path> <output_path> <operation>")
        print("Operaciones disponibles: average_price, data_organization, inverted_index, advanced_analysis")
        sys.exit(1)

    # Obtener rutas y operación desde los argumentos
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    operation = sys.argv[3]

    # Crear directorios si no existen
    os.makedirs(output_path, exist_ok=True)

    # Llamar a la función de Spark con la operación seleccionada
    spark.run_spark_analysis(input_path, output_path, operation)

if __name__ == "__main__":
    main()
