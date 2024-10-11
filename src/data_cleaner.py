# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:52:47 2024

@author: raphy
"""
import numpy as np
import pandas as pd

df = pd.read_csv("..\data\World Energy Consumption.csv")
#print(df.info())
#print(df.head())

columns = df.columns

def renewable_energy_production_frame(df):
    # country, year, bio_fuel, hydro, renewables, other_renewables, solar, wind, electricity_demand, electricity_demand_per_capita, electricity_generation
    pass
def renewable_energy_consumption_frame(df):
    # country, year, bio_fuel, hydro, renewables, other_renewables, solar, wind
    pass

def GDP_and_fossil_energy_consumption(df):
    # coal, fossil gas, oil, GDP, country
    df_fossil_energy = df[['country','year','gdp','coal_cons_per_capita','fossil_energy_per_capita','gas_energy_per_capita','oil_energy_per_capita']]
    
    # Remoção das linhas que não contem dados relativos à verificação
    no_nulls_rows = df_fossil_energy.dropna(subset=['coal_cons_per_capita','fossil_energy_per_capita','gas_energy_per_capita','oil_energy_per_capita'], how='all')
    
    # array de países ou conjuntos agrupados onde o PIB não consta em nenhum dos anos verificados
    null_gdp_countries = df.groupby('country').filter(lambda x: x['gdp'].isna().all())['country'].unique()
    
    # DataFrame sem ps países e agrupados cujo PIB não consta
    new_df = no_nulls_rows[~no_nulls_rows['country'].isin(null_gdp_countries)]
    
    return new_df



def GDP_and_fossil_energy_production(df):
    # coal, fossil gas, oil, GDP, country
    df_fossil_energy = df[['country','year','gdp','coal_prod_per_capita','fossil_elec_per_capita','gas_prod_per_capita','oil_prod_per_capita']]
    
    # Remoção das linhas que não contem dados relativos à verificação
    no_nulls_rows = df_fossil_energy.dropna(subset=['coal_prod_per_capita','fossil_elec_per_capita','gas_prod_per_capita','oil_prod_per_capita'], how='all')
    
    # array de países ou conjuntos agrupados onde o PIB não consta em nenhum dos anos verificados
    null_gdp_countries = df.groupby('country').filter(lambda x: x['gdp'].isna().all())['country'].unique()
    
    # DataFrame sem ps países e agrupados cujo PIB não consta
    new_df = no_nulls_rows[~no_nulls_rows['country'].isin(null_gdp_countries)]
    
    return new_df    





def correlations_counts(df):
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
    
    return correlation_counts_df




GDP_and_fossil_energy_frame = GDP_and_fossil_energy_consumption(df)


# Limpeza de dados para a Hipótese 3
def demand_and_production(df):
    # Colunas necessárias para a análise 
    df_columns_needed = df[['country','year','electricity_demand','renewables_electricity']]
    
    # Eliminação das linhas que não contenham a demanda ou a produção
    no_nulls_rows = df_columns_needed.dropna(subset=['electricity_demand','renewables_electricity'], how='any')
    
    # Praticamente todos países contém dados entre 2000 e 2021, então a analíse será feita nesse período 
    df_clean = no_nulls_rows[(no_nulls_rows['year'] >= 2000) & (no_nulls_rows['year'] <= 2021)]
    
    return df_clean

demand_production_frame = demand_and_production(df)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
