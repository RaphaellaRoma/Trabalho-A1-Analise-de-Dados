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
    
countries_by_continent_map = {
    "Antarctica": ["Antarctica"],
    "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", "Congo", "Cote d'Ivoire", "Democratic Republic of Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
    "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"],
    "Europe": ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom"],
    "North America": ["Canada", "Greenland", "Mexico", "United States"],
    "Central America": ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago"],
    "South America": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
    "Oceania": ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
}

# Filters lines that are countries and are defined in the dictionary
def continent_identifier(country: str) -> str:
    """
    Identifies the continent of a country.

    Parameters
    ----------
    country : str
        The name of the country.

    Returns
    -------
    str
        The continent of the country.

    Examples
    --------
    >>> continent_identifier("Brazil")
    South America
    >>> continent_identifier("Vanuatu")
    Oceania
    """
    for continent, countries in countries_by_continent_map.items():
        if country in countries:
            return continent
    return None

# Aggregates the data of the countries by continent
def renewable_energy_consumption_by_continent(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a new DataFrame with data from each continent without empty lines.

    Parameters
    ----------
    df: pd.DataFrame
        The original DataFrame.

    Returns
    -------
    pd.DataFrame
        The new DataFrame with the data of the continents.
    """
    # Creates a new column with the continent of each country
    df["continent"] = df["country"].apply(continent_identifier)
    # Filters the columns of interest
    df_continents = df[["continent", "year", "biofuel_consumption", "hydro_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"]]
    # Filters the lines without empty values
    no_nulls_rows = df_continents.dropna(subset=["biofuel_consumption", "hydro_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"], how='any')
    # Filters the valid lines with years between 1990 and 2024
    new_df = no_nulls_rows[(no_nulls_rows['year'] >= 1990) & (no_nulls_rows['year'] <= 2024)]
    return new_df

# Calls the function to create the new DataFrame
renewable_energy_consumption_continental = renewable_energy_consumption_by_continent(df)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
