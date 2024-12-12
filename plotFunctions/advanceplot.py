import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def plot_combined_csvs():
    # Ocultar la ventana principal de Tkinter
    Tk().withdraw()

    # Seleccionar el primer CSV
    csv_file_path_1 = filedialog.askopenfilename(title="Select First CSV File (Trend Data)", filetypes=[("CSV files", "*.csv")])
    if not csv_file_path_1:
        print("No file selected for Trend Data. Exiting.")
        return

    # Seleccionar el segundo CSV
    csv_file_path_2 = filedialog.askopenfilename(title="Select Second CSV File (Ranked Data)", filetypes=[("CSV files", "*.csv")])
    if not csv_file_path_2:
        print("No file selected for Ranked Data. Exiting.")
        return

    # Seleccionar la ubicación para guardar el gráfico
    output_file_path = filedialog.asksaveasfilename(title="Save Plot As", defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf"),
                                                                ("JPG files", "*.jpg"), ("SVG files", "*.svg")])
    if not output_file_path:
        print("No save location selected. Exiting.")
        return

    # Leer el primer CSV
    df_trend = pd.read_csv(csv_file_path_1, parse_dates=['Date'])
    print("First CSV (Trend Data):")
    print(df_trend.head())

    # Leer el segundo CSV
    df_ranked = pd.read_csv(csv_file_path_2)
    print("\nSecond CSV (Ranked Data):")
    print(df_ranked.head())

    # Crear la figura
    plt.figure(figsize=(14, 7))

    # Gráfico de línea para Close y CumulativeClose
    plt.subplot(2, 1, 1)
    plt.plot(df_trend['Date'], df_trend['Close'], marker='o', linestyle='-', color='blue', label='Close Price')
    plt.plot(df_trend['Date'], df_trend['CumulativeClose'], marker='o', linestyle='--', color='orange', label='Cumulative Close')
    plt.title('Close and Cumulative Close Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    # Gráfico de barras para AvgClose con Rank
    plt.subplot(2, 1, 2)
    plt.bar(df_ranked['Year'].astype(str), df_ranked['AvgClose'], color='green', label='Average Close Price')
    for i, rank in enumerate(df_ranked['Rank']):
        plt.text(i, df_ranked['AvgClose'][i], f'Rank: {rank}', ha='center', va='bottom')
    plt.title('Average Close Price with Rank')
    plt.xlabel('Year')
    plt.ylabel('Average Close Price')
    plt.grid(True)

    # Ajustar diseño y guardar la figura
    plt.tight_layout()
    plt.savefig(output_file_path)
    plt.close()

# Ejecutar la función
plot_combined_csvs()
