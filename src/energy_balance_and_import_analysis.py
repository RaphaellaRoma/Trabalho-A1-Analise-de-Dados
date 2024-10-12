import numpy as np
import data_cleaner
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_main = pd.DataFrame(data_cleaner.balance_import)

def plot_energy_balance_import(df_main):

    # Criando um df_annual_energy_balance com os dados totais do balanço de energia por ano
    df_annual_energy_balance_by_country = pd.DataFrame()
    
    df_annual_energy_balance_by_country["year"] = df_main["year"]
    df_annual_energy_balance_by_country["energy_balance"] = df_main["energy_balance"]
    
    df_annual_energy_balance = df_main.groupby("year")["energy_balance"].sum().reset_index()
    
    # Criando um df_annual_imports com os dados totais de importação por ano
    df_annual_imports_by_country = pd.DataFrame()
    
    df_annual_imports_by_country["year"] = df_main["year"]
    df_annual_imports_by_country["net_elec_imports"] = df_main["net_elec_imports"]
    
    df_annual_imports = df_main.groupby("year")["net_elec_imports"].sum().reset_index()

    # Criando um df_annual_consumption_and_population com os dados totais de importação por ano e de balanço de energia por ano
    df_annual_energy_balance_and_import = pd.DataFrame()
    
    df_annual_energy_balance_and_import["year"] = df_annual_energy_balance["year"]
    df_annual_energy_balance_and_import["energy_balance"] = df_annual_energy_balance["energy_balance"]
    df_annual_energy_balance_and_import["net_elec_imports"] = df_annual_imports["net_elec_imports"]

    # Gráfico de linhas para o balanço de energia e importação
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(df_annual_energy_balance_and_import["year"], df_annual_energy_balance_and_import["energy_balance"], label="Balanço de energia", color="blue")
    ax1.set_title("Balanço de energia ao Longo dos Anos")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Values")
    ax1.legend()

    ax2.plot(df_annual_energy_balance_and_import["year"], df_annual_energy_balance_and_import["net_elec_imports"], label="Importações", color="purple")
    ax2.set_title("Importação ao Longo dos Anos")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Values")
    ax2.legend()
    
    return fig
