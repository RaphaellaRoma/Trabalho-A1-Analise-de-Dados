# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:52:50 2024

@author: raphy
"""
import numpy as np
import data_cleaner
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame(data_cleaner.GDP_and_fossil_energy_frame)
# df.set_index("country", inplace= True)
#df.drop('World', axis=0, inplace=True)



print(df.index)
columns = df.columns

df_auxiliary = df.set_index(['country', 'year']).drop("Sri Lanka").drop("Iceland").drop("Cyprus")
# o Sri Lanka e outros foram removidos pois não possuem dados suficientes de consumo para serem representativos


def plot_country_energy_gdp(df, country, ax, column, colors):
    """Plota o consumo de energia fóssil e PIB para um determinado país."""
    paises_selecionados = df.loc[country]
    
    # Gráfico de linhas para o consumo de energia fóssil
    sns.lineplot(data=paises_selecionados, x=paises_selecionados.index.get_level_values('year'),
                 y=column, marker='o', linestyle='--', ax=ax, color= colors[0], label='Energia Fóssil')
    
    # Gráfico de linhas para o PIB em um outro eixo
    ax2 = ax.twinx()
    sns.lineplot(data=paises_selecionados, x=paises_selecionados.index.get_level_values('year'),
                 y='gdp', marker='o', ax=ax2, color= colors[1], label='PIB')

    # Configurações dos eixos
    ax.set_title(f'{country}')
    ax.set_ylabel('Energia Fóssil per capita')
    ax2.set_ylabel('PIB')
    
    
    
    
    
    
# Função para plotar os 9 países com maior consumo de energia fóssil
def plot_top_9_countries(df):
    """Plota um grid dos 9 países com maior consumo médio de energia fóssil."""
    
#    df.set_index(['country', 'year'], inplace=True)
    
    # Calculo da média de consumo de energia fóssil per capita de cada país
    media_consumo = df.groupby('country')['fossil_energy_per_capita'].mean()

    # Selecionar os 9 países com o maior consumo médio
    top_9_countries = media_consumo.nlargest(9).index

    # Criar o grid de gráficos (3x3)
    fig, axes = plt.subplots(3, 3, figsize=(20, 12), sharex=True, sharey=False)

    fig.tight_layout(pad=5.0)
    colors = ['b','g']
    
    # Plotar cada país em um subplot
    for i, country in enumerate(top_9_countries):
        ax = axes[i//3, i%3]  # Selecionar o subplot correspondente
        plot_country_energy_gdp(df, country, ax, 'fossil_energy_per_capita', colors)


    fig.suptitle('Consumo de Energia Fóssil e PIB dos 9 Países com Maior Consumo Médio de Energia Fóssil', fontsize=16)

   
    plt.savefig('../plots/top_9_countries.png', dpi=300, format='png')
    plt.show()
    plt.close()






# Função para plotar os 9 países com menor consumo de energia fóssil
def plot_lower_9_countries(df):
    """Plota um grid dos 9 países com menor consumo médio de energia fóssil."""
    
#    df.set_index(['country', 'year'], inplace=True)
    
    # Calculo da média de consumo de energia fóssil per capita para cada país
    media_consumo = df.groupby('country')['fossil_energy_per_capita'].mean()

    # Selecionar os 9 países com o menor consumo médio
    lower_9_countries = media_consumo.nsmallest(9).index

    # Criar o grid de gráficos (3x3)
    fig, axes = plt.subplots(3, 3, figsize=(20, 12), sharex=True, sharey=False)


    fig.tight_layout(pad=5.0)
    colors = ['brown','orange']
    
    # Plotar cada país em um subplot
    for i, country in enumerate(lower_9_countries):
        ax = axes[i//3, i%3]  # Selecionar o subplot correspondente
        plot_country_energy_gdp(df, country, ax, 'fossil_energy_per_capita', colors)

    fig.suptitle('Consumo de Energia Fóssil e PIB dos 9 Países com Menor Consumo Médio de Energia Fóssil', fontsize=16)

   
    plt.savefig('../plots/lower_9_countries.png', dpi=300, format='png')
    plt.show()
    plt.close()
    
    

plot_top_9_countries(df_auxiliary)
plot_lower_9_countries(df_auxiliary)



def world(df, energy):
    """Plota o consumo de energia fóssil e PIB no Mundo"""
    # Criar a figura e os eixos
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ["r","b"]
    
    plot_country_energy_gdp(df,"World", ax, energy, colors)
    
    fig.tight_layout(pad=5.0)

    plt.show()


# world(df_auxiliary, 'fossil_energy_per_capita')   
    
# world(df_auxiliary, 'coal_cons_per_capita')

# world(df_auxiliary, 'gas_energy_per_capita')

# world(df_auxiliary, 'oil_energy_per_capita')



def energy_gdp_correlation(df):


    correlation_counts_df = data_cleaner.correlations_counts(df)


    correlation_counts_df.set_index('Energy Type').plot(kind='bar', figsize=(10, 6))
    plt.title('Contagem de Países por Correlação entre PIB e Consumo de Energia Fóssil')
    plt.xlabel('Tipo de Energia')
    plt.ylabel('Número de Países')
    plt.xticks(rotation=0)
    plt.legend(title='Tipo de Correlação')
    
    plt.savefig('../plots/correlations_counts.png', dpi=300, format='png')
    plt.show()
    plt.close()


energy_gdp_correlation(df)





