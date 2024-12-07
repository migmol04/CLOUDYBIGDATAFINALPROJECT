import os
import sys
import AveragePrice
import DataOrganization
import InvertedIndex
import advanced_analysis

def main():
    # Obtener rutas desde los argumentos
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Crear directorios si no existen
    os.makedirs(output_path, exist_ok=True)

    # Llamar a la función de análisis
    #AveragePrice.average_close_per_year(input_path, output_path)
    #DataOrganization.reorganize_data(input_path, output_path) 
    #InvertedIndex.inverted_index_max_close(input_path, output_path) 
    advanced_analysis.advanced_analysis(input_path, output_path)

if __name__ == "__main__":
    main()
