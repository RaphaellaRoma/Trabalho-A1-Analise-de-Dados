import pandas as pd
import data_cleaner as dc
import analise 1
import continent_consumption_analysis as cca
import demand_production_analysis as dpa   
import fossil_energy_analysis as fea

data_path = ".\data\World Energy Consumption.csv"

try:
    # Load the dataset
    df = pd.read_csv(data_path)

    # Clean the data
    clean_df = dc.clean_data(df)
    
    # Analyze renewable energy consumption by continent
    continent_df = cca.renewable_energy_consumption_by_continent(clean_df)
    
    # Analyze demand and production
    demand_production_df = dpa.demand_and_production(clean_df)
    
    # Analyze fossil energy consumption and GDP
    fossil_gdp_df = fea.GDP_and_fossil_energy_consumption(clean_df)
    
    # Output or save your results as needed
    print("Renewable energy consumption by continent:")
    print(continent_df.head())

    print("Demand and production data:")
    print(demand_production_df.head())

    print("Fossil energy consumption and GDP data:")
    print(fossil_gdp_df.head())

except FileNotFoundError:
    print("The filepath is incorrect.")