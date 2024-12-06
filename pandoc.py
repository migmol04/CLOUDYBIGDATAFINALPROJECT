import os

def generate_pandoc_document(output_path, document_path):
    # Crear el contenido en Markdown
    markdown_content = f"""
# Análisis Financiero Avanzado

## Top 3 Años con Mayor Promedio de Cierre
![Top 3 Años](ranked_years.png)

## Tendencia Acumulativa de Cierre
![Tendencia Acumulativa](trend_analysis.png)

*Este documento fue generado automáticamente usando Pandoc y PySpark.*
    """

    markdown_file = os.path.join(output_path, "analysis_report.md")
    with open(markdown_file, "w") as f:
        f.write(markdown_content)

    # Ejecutar Pandoc para generar un PDF
    os.system(f"pandoc {markdown_file} -o {document_path}/analysis_report.pdf --pdf-engine=xelatex")
