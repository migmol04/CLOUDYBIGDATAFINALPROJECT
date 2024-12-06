import matplotlib.pyplot as plt

def plot_ranked_years(ranked_years_pd, output_path):
    # Gráfico de barras para el ranking de años
    plt.figure(figsize=(10, 6))
    plt.bar(ranked_years_pd["Year"], ranked_years_pd["AvgClose"], color='skyblue')
    plt.title("Top 3 Años con Mayor Promedio de Cierre")
    plt.xlabel("Año")
    plt.ylabel("Promedio de Cierre (Close)")
    plt.savefig(f"{output_path}/ranked_years.png")
    plt.close()

def plot_trend_analysis(trend_analysis_pd, output_path):
    # Gráfico de líneas para la tendencia acumulativa
    plt.figure(figsize=(12, 8))
    for year in trend_analysis_pd["Year"].unique():
        year_data = trend_analysis_pd[trend_analysis_pd["Year"] == year]
        plt.plot(year_data["Date"], year_data["CumulativeClose"], label=f"Año {year}")

    plt.title("Tendencia Acumulativa de Cierre")
    plt.xlabel("Fecha")
    plt.ylabel("Cierre Acumulativo (Close)")
    plt.legend()
    plt.savefig(f"{output_path}/trend_analysis.png")
    plt.close()
