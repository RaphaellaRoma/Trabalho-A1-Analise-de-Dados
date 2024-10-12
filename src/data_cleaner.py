import numpy as np
import pandas as pd

df = pd.read_csv(".\data\World Energy Consumption.csv")
#print(df.info())
#print(df.head())

columns = df.columns

def GDP_and_fossil_energy_consumption(df):
    """
    Gera um df agrupado por país com todas colunas necessárias para a análise 

    Parameters
    ----------
    df : TYPE

    Returns
    -------
    new_df : TYPE

    """
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
    """
    Gera um novo df com as colunas necessárias para a análise 

    Parameters
    ----------
    df : TYPE

    Returns
    -------
    df_clean : TYPE

    """
    # A coluna country contém continentes e blocos econômicos, como só queremos analisar os países vamos eliminar os que não são
    # Criamos uma lista com todos os nomes que aparecem na coluna country
    # unique_countries = df['country'].unique().tolist() 
    # print(unique_countries)
    # Usando o chatgpt para avaliar quais nomes não são de países, geramos a lista non_countries
    non_countries = [
    'ASEAN (Ember)', 'Africa', 'Africa (EI)', 'Africa (Ember)', 'Africa (Shift)', 
    'Asia', 'Asia & Oceania (EIA)', 'Asia (Ember)', 'Asia Pacific (EI)', 
    'Asia and Oceania (Shift)', 'Australia and New Zealand (EIA)', 'CIS (EI)', 
    'Central & South America (EIA)', 'Central America (EI)', 'Central and South America (Shift)', 
    'Democratic Republic of Congo', 'EU28 (Shift)', 'East Germany (EIA)', 'Eastern Africa (EI)', 
    'Eurasia (EIA)', 'Eurasia (Shift)', 'Europe', 'Europe (EI)', 'Europe (Ember)', 
    'Europe (Shift)', 'European Union (27)', 'European Union (EIA)', 'Falkland Islands', 
    'G20 (Ember)', 'G7 (Ember)', 'Hawaiian Trade Zone (EIA)', 'High-income countries', 
    'IEO - Africa (EIA)', 'IEO - Middle East (EIA)', 'IEO OECD - Europe (EIA)', 
    'Latin America and Caribbean (Ember)', 'Low-income countries', 'Lower-middle-income countries', 
    'Mexico, Chile, and other OECD Americas (EIA)', 'Middle Africa (EI)', 'Middle East (EI)', 
    'Middle East (EIA)', 'Middle East (Ember)', 'Middle East (Shift)', 'Non-OECD (EI)', 
    'Non-OECD (EIA)', 'Non-OPEC (EI)', 'Non-OPEC (EIA)', 'North America', 'North America (EI)', 
    'North America (Ember)', 'North America (Shift)', 'OECD (EI)', 'OECD (EIA)', 'OECD (Ember)', 
    'OECD (Shift)', 'OECD - Asia And Oceania (EIA)', 'OECD - Europe (EIA)', 'OECD - North America (EIA)', 
    'OPEC (EI)', 'OPEC (EIA)', 'OPEC (Shift)', 'OPEC - Africa (EIA)', 'OPEC - South America (EIA)', 
    'Oceania', 'Oceania (Ember)', 'Other Non-OECD - America (EIA)', 'Other Non-OECD - Asia (EIA)', 
    'Other Non-OECD - Europe and Eurasia (EIA)', 'Persian Gulf (EIA)', 'Persian Gulf (Shift)', 
    'South and Central America (EI)', 'South America', 'South Korea and other OECD Asia (EIA)', 
    'U.S. Pacific Islands (EIA)', 'U.S. Territories (EIA)', 'USSR', 'United States Pacific Islands (Shift)', 
    'United States Territories (Shift)', 'Upper-middle-income countries', 'Wake Island (EIA)', 
    'Wake Island (Shift)', 'West Germany (EIA)', 'Western Africa (EI)', 'World', 'Yugoslavia'
     ]
    # Agora tiramso todas as linhas do df que comtém qualquer um desses não países
    df = df[~df['country'].isin(non_countries)]
    
    # Colunas necessárias para a análise 
    df_columns_needed = df[['country','year','gdp','electricity_demand','renewables_electricity']]
    
    # Eliminação das linhas que não contenham a demanda ou a produção
    no_nulls_rows = df_columns_needed.dropna(subset=['electricity_demand','renewables_electricity'], how='any')
    
    # Praticamente todos países contém dados entre 2000 e 2021, então a análise será feita nesse período 
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

# Filters rows that are countries and are defined in the dictionary
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
    df_continents = df[["continent", "year", "population", "biofuel_consumption", "hydro_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"]]
    # Filters the rows that have no data in the columns of interest
    filtered_df = df_continents.dropna(subset=["biofuel_consumption", "hydro_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"], how='all')
    # Filters the rows that have no data in the population column
    null_population_continents = df.groupby("continent").filter(lambda x: x["population"].isna().all())["continent"].unique()
    # Junta os filtros e coloca o intervalo de tempo desejado
    new_df = filtered_df[~filtered_df["continent"].isin(null_population_continents) & (filtered_df["year"].between(1990, 2024))]
    return new_df

# Calls the function to create the new DataFrame
renewable_energy_consumption_continental = renewable_energy_consumption_by_continent(df)

    
# Limpeza de dados para a Hipótese 1
def consumption_and_population(df):
    
    # Colunas necessárias para a análise
    df_consumption_and_population = df[["country", "year", "population", "primary_energy_consumption"]]
    
    # Eliminação das linhas que não contém o consumo e as populações
    no_nulls_row = df_consumption_and_population.dropna(subset=["population", "primary_energy_consumption"], how="any")
    
    # Todos os dados de no_nulls_row são necessários para a análise
    df_clean = no_nulls_row
    
    return df_clean

consumption_population = consumption_and_population(df)

def energy_balance_and_import(df):
    
    # Criação do total de produções baseado nas colunas de produções informadas no df
    df_productions = pd.DataFrame()    
    df_productions["total_productions"] = df["coal_production"] + df["gas_production"] + df["oil_production"]
    
    # Criação do balanço de energia baseada na coluna da demanda de eletricidade informada no df e na coluna do total de produção informada em df_productions
    df_energy_balance = pd.DataFrame()
    df_energy_balance["energy_balance"] = df["electricity_demand"] - df_productions["total_productions"]
    
    # Colunas necessárias para a análise
    df_energy_balance_and_import = pd.DataFrame()

    df_energy_balance_and_import["year"] = df[["year"]]
    df_energy_balance_and_import["energy_balance"] = df_energy_balance["energy_balance"]
    df_energy_balance_and_import["net_elec_imports"] = df["net_elec_imports"]
    
    # Eliminação das linhas que não contém o balanço de energia e as importações
    no_nulls_row = df_energy_balance_and_import.dropna(subset=["energy_balance", "net_elec_imports"], how="any")
    
    # Quando energy_balance e net_elec_imports são positivos, significa que houve demanda reprimida ou necessidade de importação, então a análise será feita para ambos os dados positivos
    df_clean = no_nulls_row[(no_nulls_row["energy_balance"] > 0) & (no_nulls_row["net_elec_imports"] > 0)]
    
    return df_clean

balance_import = energy_balance_and_import(df)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
