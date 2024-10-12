import numpy as np
import data_cleaner
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carrega o DataFrame principal usando os dados do data_cleaner
df_main = pd.DataFrame(data_cleaner.consumption_population)

def plot_consumption_population(df_main: pd.DataFrame) -> plt.Figure:
    """
    Gera gráficos de linhas para o consumo de energia e a população ao longo dos anos.

    A função cria dois gráficos:
      - O primeiro gráfico exibe o consumo total de energia por ano.
      - O segundo gráfico exibe a população total por ano.

    Parâmetros:
    -----------
    df_main : pd.DataFrame
        DataFrame contendo as colunas 'year', 'primary_energy_consumption' e 'population'.

    Retorno:
    --------
    matplotlib.figure.Figure
        Objeto Figure do Matplotlib contendo os gráficos gerados.
    """

    # Cria um DataFrame com o consumo de energia por ano e por país
    df_annual_consumption_by_country = pd.DataFrame({
        "year": df_main["year"],
        "primary_energy_consumption": df_main["primary_energy_consumption"]
    })

    # Agrupa por 'year' para obter o consumo total por ano
    df_annual_consumption = (
        df_annual_consumption_by_country
        .groupby("year")["primary_energy_consumption"]
        .sum()
        .reset_index()
    )

    # Cria um DataFrame com a população por ano e por país
    df_annual_population_by_country = pd.DataFrame({
        "year": df_main["year"],
        "population": df_main["population"]
    })

    # Agrupa por 'year' para obter a população total por ano
    df_annual_population = (
        df_annual_population_by_country
        .groupby("year")["population"]
        .sum()
        .reset_index()
    )

    # Combina os dados de consumo de energia e população em um único DataFrame
    df_annual_consumption_and_population = pd.DataFrame({
        "year": df_annual_consumption["year"],
        "primary_energy_consumption": df_annual_consumption["primary_energy_consumption"],
        "population": df_annual_population["population"]
    })

    # Cria dois gráficos de linha lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Gráfico de consumo de energia ao longo dos anos
    ax1.plot(
        df_annual_consumption_and_population["year"],
        df_annual_consumption_and_population["primary_energy_consumption"],
        label="Consumo de energia", color="blue"
    )
    ax1.set_title("Consumo de Energia ao Longo dos Anos")
    ax1.set_xlabel("Ano")
    ax1.set_ylabel("Consumo de Energia")
    ax1.legend()

    # Gráfico de população ao longo dos anos
    ax2.plot(
        df_annual_consumption_and_population["year"],
        df_annual_consumption_and_population["population"],
        label="População", color="orange"
    )
    ax2.set_title("População ao Longo dos Anos")
    ax2.set_xlabel("Ano")
    ax2.set_ylabel("População")
    ax2.legend()

    # Retorna o objeto Figure contendo os gráficos
    return fig
