import os
import sys
import advanced_analysis
from matplot import plot_ranked_years, plot_trend_analysis
from pandoc import generate_pandoc_document
def main():
    # Verificar argumentos de entrada
    if len(sys.argv) != 4:
        print("Uso: python script.py <input_path> <output_path> <document_path>")
        sys.exit(1)

    # Obtener rutas desde los argumentos
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    document_path = sys.argv[3]

    # Crear directorios si no existen
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(document_path, exist_ok=True)

    # Realizar el análisis
    ranked_years_pd, trend_analysis_pd = advanced_analysis(input_path)

    # Crear gráficos
    plot_ranked_years(ranked_years_pd, output_path)
    plot_trend_analysis(trend_analysis_pd, output_path)

    # Generar el documento final
  #  generate_pandoc_document(output_path, document_path)
