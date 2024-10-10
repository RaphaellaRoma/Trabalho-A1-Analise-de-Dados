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
# df.drop('World', axis=0, inplace=True)

print(df.index)
columns = df.columns

# df.set_index(['country', 'year'], inplace=True)



def plot_country_energy_gdp(df, country, ax, colors):
    """Plota o consumo de energia fóssil e PIB para um determinado país."""
    paises_selecionados = df.loc[country]

    # Gráfico de linhas para o consumo de energia fóssil
    sns.lineplot(data=paises_selecionados, x=paises_selecionados.index.get_level_values('year'),
                 y='fossil_energy_per_capita', marker='o', linestyle='--', ax=ax, color= colors[0], label='Energia Fóssil')

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
    
    df.set_index(['country', 'year'], inplace=True)
    
    # Calcular a média de consumo de energia fóssil per capita para cada país
    media_consumo = df.groupby('country')['fossil_energy_per_capita'].mean()

    # Selecionar os 9 países com o maior consumo médio
    top_9_countries = media_consumo.nlargest(9).index

    # Criar o grid de gráficos (3x3)
    fig, axes = plt.subplots(3, 3, figsize=(20, 12), sharex=True, sharey=False)

    # Ajustar o layout
    fig.tight_layout(pad=5.0)
    colors = ['b','g']
    
    # Loop pelos 9 países para plotar cada um em um subplot
    for i, country in enumerate(top_9_countries):
        ax = axes[i//3, i%3]  # Selecionar o subplot correspondente
        plot_country_energy_gdp(df, country, ax, colors)

    # Título geral
    fig.suptitle('Consumo de Energia Fóssil e PIB dos 9 Países com Maior Consumo Médio de Energia Fóssil', fontsize=16)

   
    plt.savefig('../plots/top_9_countries.png', dpi=300, format='png')
    plt.show()
    plt.close()






# Função para plotar os 9 países com menor consumo de energia fóssil
def plot_lower_9_countries(df):
    """Plota um grid dos 9 países com menor consumo médio de energia fóssil."""
    
    df.set_index(['country', 'year'], inplace=True)
    
    # Calcular a média de consumo de energia fóssil per capita para cada país
    media_consumo = df.groupby('country')['fossil_energy_per_capita'].mean()

    # Selecionar os 9 países com o menor consumo médio
    lower_9_countries = media_consumo.nsmallest(9).index

    # Criar o grid de gráficos (3x3)
    fig, axes = plt.subplots(3, 3, figsize=(20, 12), sharex=True, sharey=False)

    # Ajustar o layout
    fig.tight_layout(pad=5.0)
    colors = ['brown','orange']
    
    # Loop pelos 9 países para plotar cada um em um subplot
    for i, country in enumerate(lower_9_countries):
        ax = axes[i//3, i%3]  # Selecionar o subplot correspondente
        plot_country_energy_gdp(df, country, ax, colors)

    # Título
    fig.suptitle('Consumo de Energia Fóssil e PIB dos 9 Países com Menor Consumo Médio de Energia Fóssil', fontsize=16)

   
    plt.savefig('../plots/lower_9_countries.png', dpi=300, format='png')
    plt.show()
    plt.close()
# Chamar a função para plotar o grid dos 9 países
plot_lower_9_countries(df)
