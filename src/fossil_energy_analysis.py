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

df_auxiliary = df.set_index(['country', 'year'])



def plot_country_energy_gdp(df, country, ax, column, colors):
    """
    Plota o consumo de energia fóssil e o PIB para um determinado país ao longo do tempo.

    Parameters
    ----------
    df : DataFrame
        DataFrame com os dados de energia e PIB.
    country : str
        Nome do país a ser plotado.
    ax : matplotlib.axes.Axes
        Eixo para plotar o gráfico de consumo de energia fóssil.
    column : str
        Coluna do DataFrame que representa o consumo de energia fóssil per capita.
    colors : list
        Lista de cores para o gráfico. A primeira cor será usada para o consumo de energia, 
        e a segunda cor será usada para o PIB.

    Returns
    -------
    None.
        A função plota o gráfico, sem retornar valores.
    """
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
    """
    Plota um grid 3x3 dos 9 países com maior consumo médio de energia fóssil per capita.

    Parameters
    ----------
    df : DataFrame
        DataFrame com os dados de energia e PIB, agrupados por país e ano.

    Returns
    -------
    None.
        O gráfico é salvo como um arquivo PNG no diretório '../plots/'.
    """
    
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
    """
    Plota um grid 3x3 dos 9 países com menor consumo médio de energia fóssil per capita.

    Parameters
    ----------
    df : DataFrame
        DataFrame com os dados de energia e PIB, agrupados por país e ano.

    Returns
    -------
    None.
        O gráfico é salvo como um arquivo PNG no diretório '../plots/'.
    """
    
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
    """
    Plota o consumo de energia fóssil e o PIB global ao longo do tempo.

    Parameters
    ----------
    df : DataFrame
        DataFrame com os dados de energia e PIB.
    energy : str
        Coluna do DataFrame que representa o tipo de energia a ser plotado (e.g., 'fossil_energy_per_capita').

    Returns
    -------
    None.
        A função plota o gráfico, sem retornar valores.
    """
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
    """
    Calcula e plota as contagens de países classificados por níveis de correlação (alta, moderada e baixa) entre PIB e consumo de diferentes tipos de energia fóssil.

    Parameters
    ----------
    df : DataFrame
        DataFrame com os dados de energia e PIB, agrupados por país.

    Returns
    -------
    None.
        O gráfico de barras é salvo como um arquivo PNG no diretório '../plots/'.
    """
    # Dicionário para armazenar as contagens de correlação
    correlation_counts = {
        'Energy Type': [],
        'Alta Correlação': [],
        'Correlação Moderada': [],
        'Baixa Correlação': []
    }

    # Calcular as contagens para cada tipo de energia
    for energy, col in zip(['Carvão', 'Gás', 'Petróleo'], 
                            ['coal_cons_per_capita', 'gas_energy_per_capita', 'oil_energy_per_capita']):
        counts = {'high': 0, 'moderate': 0, 'low': 0}

        # Agrupar por país
        for country, group in df.groupby('country'):
            group_clean = group.dropna(subset=['gdp', col])
            if len(group_clean) > 1:
                corr_matrix = group_clean[['gdp', col]].corr()
                correlation_value = corr_matrix.iloc[0, 1]

                # Classificar a correlação
                if abs(correlation_value) > 0.7:
                    counts['high'] += 1
                elif abs(correlation_value) > 0.3:
                    counts['moderate'] += 1
                else:
                    counts['low'] += 1

        # Adicionar os resultados ao dicionário de contagens
        correlation_counts['Energy Type'].append(energy)
        correlation_counts['Alta Correlação'].append(counts['high'])
        correlation_counts['Correlação Moderada'].append(counts['moderate'])
        correlation_counts['Baixa Correlação'].append(counts['low'])

    # DataFrame das contagens
    correlation_counts_df = pd.DataFrame(correlation_counts)


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
