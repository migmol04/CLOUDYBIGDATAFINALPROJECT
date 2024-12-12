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
    output_directory = filedialog.askdirectory(title="Select Directory to Save Plots")
    if not output_directory:
        print("No save location selected. Exiting.")
        return

    # Leer los datos desde el archivo CSV
    df = pd.read_csv(csv_file_path)

    # Ordenar los datos por 'Year'
    df = df.sort_values(by='Year')

    # Mostrar un resumen estadístico del DataFrame
    print(df.describe())

    # Gráfico 1: Gráfico de líneas para visualizar AvgClose a lo largo de los años
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['AvgClose'], marker='o', linestyle='-', color='orange', label='AvgClose')
    plt.title('Average Close Price Over the Years')
    plt.xlabel('Year')
    plt.ylabel('AvgClose')
    plt.grid(True)
    plt.legend()
    plt.xticks(df['Year'], rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_directory}/avg_close_over_years.png")
    plt.close()

    # Gráfico 2: Comparación de MinClose y MaxClose a lo largo de los años
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['MinClose'], marker='o', linestyle='-', color='red', label='MinClose')
    plt.plot(df['Year'], df['MaxClose'], marker='o', linestyle='-', color='green', label='MaxClose')
    plt.title('Min and Max Close Prices Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.xticks(df['Year'], rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_directory}/min_max_close_over_years.png")
    plt.close()

    # Gráfico 3: Gráfico de barras para AvgVolume a lo largo de los años
    plt.figure(figsize=(12, 6))
    plt.bar(df['Year'], df['AvgVolume'], color='blue', alpha=0.7, label='AvgVolume')
    plt.title('Average Volume Over the Years')
    plt.xlabel('Year')
    plt.ylabel('AvgVolume')
    plt.grid(axis='y')
    plt.legend()
    plt.xticks(df['Year'], rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_directory}/avg_volume_over_years.png")
    plt.close()

    # Gráfico 4: Gráfico de dispersión con línea de regresión para AvgClose
    coefficients = np.polyfit(df['Year'], df['AvgClose'], 1)
    polynomial = np.poly1d(coefficients)
    regression_line = polynomial(df['Year'])

    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['AvgClose'], color='orange', label='AvgClose')
    plt.plot(df['Year'], regression_line, color='blue', linestyle='--', label=f'Regression Trend (y={coefficients[0]:.2f}x + {coefficients[1]:.2f})')
    plt.title('Average Close Price with Regression Trend')
    plt.xlabel('Year')
    plt.ylabel('AvgClose')
    plt.grid(True)
    plt.legend()
    plt.xticks(df['Year'], rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_directory}/avg_close_regression.png")
    plt.close()

    print(f"Plots saved to {output_directory}")

# Ejecutar la función
analyze_and_plot_csv()
