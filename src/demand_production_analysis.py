# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:43:55 2024

@author: santo
"""
import numpy as np
import data_cleaner
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(data_cleaner.demand_production_frame)

# Agrupando todos países
df_grouped = df.groupby('year').sum().reset_index()

# Colunas que serão usadas para fazer os gráficos
df_demand_production = pd.melt(df_grouped, id_vars='year', value_vars=['electricity_demand', 'renewables_electricity'], var_name='Tipo', value_name='Valor')
    

def plot_comparison_demand_production(df):
    # Histograma que compara a demanda e a produção por ano
    sns.histplot(data=df_demand_production, x='year', hue='Tipo', weights='Valor', multiple='dodge', bins=22)
    plt.title('Comparação entre Demanda e Produção de Energia Renovável por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade')
    
    # Salvar gráfico
    plt.savefig('../plots/demand_production.png', dpi=300, format='png')
    
plot_comparison_demand_production(df)

def plot_variation_demand_production(df):
    # Calcular a taxa de variação da demanda por ano usando o método pct_change()
    df_grouped['variation_demand'] = df_grouped['electricity_demand'].pct_change() * 100
    # Calcular a taxa de variação da produção por ano usando o método pct_change()
    df_grouped['variation_production'] = df_grouped['renewables_electricity'].pct_change() * 100
    
    # Line Plot que compara a taxa de variação da demanda com a taxa de variação da produção de energia renovável por ano
    plt.figure(figsize=(10,6))
    sns.lineplot(x='year', y='variation_demand', data=df_grouped, label='Taxa de Variação - Produção', marker='o')
    sns.lineplot(x='year', y='variation_production', data=df_grouped, label='Taxa de Variação - Demanda', marker='o')

    # Adicionar títulos e rótulos
    plt.title('Comparação entre Taxa de Variação da Demanda e Taxa de Variação de Energia Renovável')
    plt.xlabel('Ano')
    plt.ylabel('Taxa de Variação (%)')
    plt.legend()
    
    # Salvar gráfico
    plt.savefig('../plots/variation_demand_production.png', dpi=300, format='png')





    