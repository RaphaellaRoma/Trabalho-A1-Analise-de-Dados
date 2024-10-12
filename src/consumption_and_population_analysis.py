import numpy as np
import data_cleaner
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_main = pd.DataFrame(data_cleaner.consumption_population)

def plot_consumption_population(df_main):

    # Criando um df_annual_consumption com os dados totais de população por ano
    df_annual_consumption_by_country = pd.DataFrame()
    
    df_annual_consumption_by_country["year"] = df_main["year"]
    df_annual_consumption_by_country["primary_energy_consumption"] = df_main["primary_energy_consumption"]
    
    df_annual_consumption = df_main.groupby("year")["primary_energy_consumption"].sum().reset_index()
    
    # Criando um df_annual_population com os dados totais de população por ano
    df_annual_population_by_country = pd.DataFrame()
    
    df_annual_population_by_country["year"] = df_main["year"]
    df_annual_population_by_country["population"] = df_main["population"]
    
    df_annual_population = df_main.groupby("year")["population"].sum().reset_index()

    # Criando um df_annual_consumption_and_population com os dados totais de população por ano e de consumo por ano
    df_annual_consumption_and_population = pd.DataFrame()
    
    df_annual_consumption_and_population["year"] = df_annual_consumption["year"]
    df_annual_consumption_and_population["primary_energy_consumption"] = df_annual_consumption["primary_energy_consumption"]
    df_annual_consumption_and_population["population"] = df_annual_population["population"]

    # Gráfico de linhas para o consumo de energia e população
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(df_annual_consumption_and_population["year"], df_annual_consumption_and_population["primary_energy_consumption"], label="Consumo de energia", color="blue")
    ax1.set_title("Consumo de energia ao Longo dos Anos")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Values")
    ax1.legend()

    ax2.plot(df_annual_consumption_and_population["year"], df_annual_consumption_and_population["population"], label="População", color="orange")
    ax2.set_title("População ao Longo dos Anos")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Values")
    ax2.legend()
    
    return fig
