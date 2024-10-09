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
    #country, year, bio_fuel, hydro, renewables, other_renewables, solar, wind
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


GDP_and_fossil_energy_frame = GDP_and_fossil_energy_consumption(df)