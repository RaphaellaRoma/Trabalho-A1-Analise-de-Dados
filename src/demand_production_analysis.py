import numpy as np
import data_cleaner
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(data_cleaner.demand_production_frame)

# Agrupando todos países
df_grouped = df.groupby('year').sum().reset_index()

def plot_comparison_demand_production(df_grouped):
    # Colunas que serão usadas para fazer o gráfico
    df_demand_production = pd.melt(df_grouped, id_vars='year', value_vars=['electricity_demand', 'renewables_electricity'], var_name='Tipo', value_name='Valor')
    # Gráfico de barras que compara a demanda e a produção por ano
    plt.figure(figsize=(10,6))
    sns.barplot(data=df_demand_production, x='year', y='Valor', hue='Tipo', dodge=True)
    plt.title('Comparação entre Demanda e Produção de Energia Renovável por Ano')
    plt.xlabel('Ano')
    plt.ylabel('TWh')
    plt.legend(title='Tipo', labels=['Demanda de Energia', 'Produção de Energia Renovável'], loc='upper left')
    plt.xticks(rotation=45)
    
    # Salvar gráfico
    plt.savefig('../plots/demand_production.png', dpi=300, format='png')
    
plot_comparison_demand_production(df_grouped)

def plot_variation_demand_production(df_grouped):
    # Calcular a taxa de variação da demanda por ano usando o método pct_change()
    df_grouped['variation_demand'] = df_grouped['electricity_demand'].pct_change() * 100
    # Calcular a taxa de variação da produção por ano usando o método pct_change()
    df_grouped['variation_production'] = df_grouped['renewables_electricity'].pct_change() * 100
    
    # Line Plot que compara a taxa de variação da demanda com a taxa de variação da produção de energia renovável por ano
    plt.figure(figsize=(10,6))
    sns.lineplot(x='year', y='variation_demand', data=df_grouped, label='Taxa de Variação - Demanda', marker='o')
    sns.lineplot(x='year', y='variation_production', data=df_grouped, label='Taxa de Variação - Produção', marker='o')

    # Adicionar títulos e rótulos
    plt.title('Comparação entre Taxa de Variação da Demanda e Taxa de Variação de Energia Renovável')
    plt.xlabel('Ano')
    plt.ylabel('Taxa de Variação (%)')
    plt.legend()
    
    # Salvar gráfico
    plt.savefig('../plots/variation_demand_production.png', dpi=300, format='png')

plot_variation_demand_production(df_grouped)    

def plot_variation_in_the_richest_countries(df):
    # Os países mais ricos serão aqueles com maior média do pib
    gdp_mean = df.groupby('country')['gdp'].mean()
    
    # País mais rico
    rich_1 = gdp_mean.idxmax()
    df_rich_1 = df[df['country'] == rich_1]
    # Calcular a taxa de variação da demanda por ano usando o método pct_change()
    df_rich_1['variation_demand'] = df_rich_1['electricity_demand'].pct_change() * 100
    # # Calcular a taxa de variação da produção por ano usando o método pct_change()
    df_rich_1['variation_production'] = df_rich_1['renewables_electricity'].pct_change() * 100
    
    # Eliminamos o país mais rico da série 
    gdp_mean = gdp_mean.drop(rich_1)
    
    # Segundo país mais rico
    rich_2 = gdp_mean.idxmax()
    df_rich_2 = df[df['country'] == rich_2]
    # Calcular a taxa de variação da demanda por ano usando o método pct_change()
    df_rich_2['variation_demand'] = df_rich_2['electricity_demand'].pct_change() * 100
    # # Calcular a taxa de variação da produção por ano usando o método pct_change()
    df_rich_2['variation_production'] = df_rich_2['renewables_electricity'].pct_change() * 100
    
    # Eliminamos o segundo país mais rico da série 
    gdp_mean = gdp_mean.drop(rich_2)
    
    # Terceiro país mais rico
    rich_3 = gdp_mean.idxmax()
    df_rich_3 = df[df['country'] == rich_3]
    # Calcular a taxa de variação da demanda por ano usando o método pct_change()
    df_rich_3['variation_demand'] = df_rich_3['electricity_demand'].pct_change() * 100
    # # Calcular a taxa de variação da produção por ano usando o método pct_change()
    df_rich_3['variation_production'] = df_rich_3['renewables_electricity'].pct_change() * 100
    
    # Line Plot que compara a taxa de variação da demanda com a taxa de variação da produção de energia renovável por ano
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    sns.lineplot(x='year', y='variation_demand', data=df_rich_1, label='Taxa de Variação - Demanda', marker='o', ax=axes[0])
    sns.lineplot(x='year', y='variation_production', data=df_rich_1, label='Taxa de Variação - Produção', marker='o', ax=axes[0])
    axes[0].set_title(f"{rich_1}")
    
    sns.lineplot(x='year', y='variation_demand', data=df_rich_2, label='Taxa de Variação - Demanda', marker='o', ax=axes[1])
    sns.lineplot(x='year', y='variation_production', data=df_rich_2, label='Taxa de Variação - Produção', marker='o', ax=axes[1])
    axes[1].set_title(f"{rich_2}")
    
    sns.lineplot(x='year', y='variation_demand', data=df_rich_3, label='Taxa de Variação - Demanda', marker='o', ax=axes[2])
    sns.lineplot(x='year', y='variation_production', data=df_rich_3, label='Taxa de Variação - Produção', marker='o', ax=axes[2])
    axes[2].set_title(f"{rich_3}")

    # Adicionar títulos e rótulos
    fig.suptitle('Comparação entre Taxa de Variação da Demanda e Taxa de Variação de Energia Renovável dos 3 países mais ricos')
    plt.xlabel('Ano')
    plt.ylabel('Taxa de Variação (%)')
    plt.legend()
    plt.xticks(rotation=45)
    
    # Salvar gráfico
    plt.savefig('../plots/variation_in_the_richest_countries.png', dpi=300, format='png')
     
plot_variation_in_the_richest_countries(df)
































    