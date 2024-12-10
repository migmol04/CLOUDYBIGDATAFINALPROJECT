import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def plot_csv_with_regression():
    Tk().withdraw()

    csv_file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
    if not csv_file_path:
        print("No file selected. Exiting.")
        return
    output_file_path = filedialog.asksaveasfilename(title="Save Plot As", defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf"),
                                                                ("JPG files", "*.jpg"), ("SVG files", "*.svg")])
    if not output_file_path:
        print("No save location selected. Exiting.")
        return

    df = pd.read_csv(csv_file_path)
    years = df['Year']
    avg_close = df['AverageClose']
    coefficients = np.polyfit(years, avg_close, 1)
    polynomial = np.poly1d(coefficients)
    regression_line = polynomial(years)
    plt.figure(figsize=(12, 6))
    plt.plot(years, avg_close, marker='o', linestyle='-', label='Average Close Price', color='orange')
    plt.plot(years, regression_line, linestyle='--', color='blue', label=f'Regression Trend (y={coefficients[0]:.2f}x + {coefficients[1]:.2f})')

    # Add title and labels
    plt.title('Average Close Price of Stocks with Regression Trend')
    plt.xlabel('Year')
    plt.ylabel('Average Close Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(years, rotation=45)
    plt.savefig(output_file_path)
    plt.close()

    print(f"Plot saved to {output_file_path}")


plot_csv_with_regression()
