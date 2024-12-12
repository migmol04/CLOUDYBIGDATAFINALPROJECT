import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def analyze_and_plot_csv():
    # Ocultar la ventana principal de Tkinter
    Tk().withdraw()

    # Seleccionar el archivo CSV
    csv_file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
    if not csv_file_path:
        print("No file selected. Exiting.")
        return

    # Seleccionar la ubicación para guardar los gráficos
    output_directory = filedialog.askdirectory(title="Select Directory to Save Plot")
    if not output_directory:
        print("No save location selected. Exiting.")
        return

    # Leer el archivo CSV sin encabezado y asignar nombres a las columnas
    df = pd.read_csv(csv_file_path, header=None, names=["Year", "MaxClose", "Date"])

    # Convertir la columna 'Date' a tipo fecha
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Ordenar los datos por 'Year'
    df = df.sort_values(by='Year')

    # Mostrar un resumen estadístico del DataFrame
    print(df.describe())

    # Gráfico: MaxClose a lo largo de los años
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['MaxClose'], marker='o', linestyle='-', color='blue', label='MaxClose')
    plt.title('Maximum Close Price Over the Years')
    plt.xlabel('Year')
    plt.ylabel('MaxClose')
    plt.grid(True)
    plt.legend()
    plt.xticks(df['Year'], rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_directory}/max_close_over_years.png")
    plt.close()

    print(f"Plot saved to {output_directory}/max_close_over_years.png")

# Ejecutar la función
analyze_and_plot_csv()
