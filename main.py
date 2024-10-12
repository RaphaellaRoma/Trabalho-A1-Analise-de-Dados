import src.data_cleaner as data_cleaner
from src.data_cleaner import GDP_and_fossil_energy_consumption, demand_and_production, continent_identifier, renewable_energy_consumption_by_continent, consumption_and_population, energy_balance_and_import
from src.demand_production_analysis import plot_comparison_demand_production, plot_variation_demand_production, plot_variation_in_the_richest_countries
from src.consumption_and_population_analysis import plot_consumption_population
from src.continent_consumption_analysis import plot_renewable_energy_consumption_continental
from src.energy_balance_and_import_analysis import plot_energy_balance_import
from src.fossil_energy_analysis import plot_country_energy_gdp, plot_top_9_countries, plot_lower_9_countries, world, energy_gdp_correlation

import pandas as pd

#df = pd.read_csv("data\World Energy Consumption.csv")
df_main = pd.DataFrame(data_cleaner.consumption_population)
df_1 = pd.DataFrame(data_cleaner.renewable_energy_consumption_continental)
df_2 = pd.DataFrame(data_cleaner.demand_production_frame)
df_grouped = df_2.groupby('year').sum().reset_index()
df_main_2 = pd.DataFrame(data_cleaner.balance_import)
df_3 = pd.DataFrame(data_cleaner.GDP_and_fossil_energy_frame)


# GDP_and_fossil_energy_consumption = GDP_and_fossil_energy_consumption(df)
# demand_and_production = demand_and_production(df)
# continent_identifier = continent_identifier()
# renewable_energy_consumption_by_continent = renewable_energy_consumption_by_continent(df)
# consumption_and_population = consumption_and_population(df)
# energy_balance_and_import = energy_balance_and_import(df)

plot_consumption_population = plot_consumption_population(df_main)
plot_renewable_energy_consumption_continental = plot_renewable_energy_consumption_continental(df_1)
plot_comparison_demand_production = plot_comparison_demand_production(df_grouped)
plot_variation_demand_production = plot_variation_demand_production(df_grouped)
plot_variation_in_the_richest_countries = plot_variation_in_the_richest_countries(df_2)
plot_energy_balance_import = plot_energy_balance_import(df_main_2)
plot_country_energy_gdp = plot_country_energy_gdp(df_3)
plot_top_9_countries = plot_top_9_countries(df_3)
plot_lower_9_countries = plot_lower_9_countries(df_3)
world = world(df_3)
energy_gdp_correlation = energy_gdp_correlation(df_3)

