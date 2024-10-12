"""Stacked Column Chart Generation Module

This module contains the graph generating function
on the consumption of renewable energy on the continents over the years.
"""

import pandas as pd
import matplotlib.pyplot as plt
import data_cleaner

df = pd.DataFrame(data_cleaner.renewable_energy_consumption_continental)

# Creates a new colum in the new DF with the sum of the different types of renewable energy
df['total_renewable_consumption'] = (
    df['biofuel_consumption'] +
    df['hydro_consumption'] +
    df['other_renewable_consumption'] +
    df['renewables_consumption'] +
    df['solar_consumption'] +
    df['wind_consumption']
)

df['renewable_consumption_per_capita'] = df['total_renewable_consumption'] / df['population']

# Plots the stacked bar chart
def plot_renewable_energy_consumption_continental(df: pd.DataFrame) -> None:
    """
    Plots a stacked bar chart with the total renewable energy consumption by continent over the years.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame with the data of the continents.
    """
    # Groups the data by year and continent
    grouped_data = df.groupby(['year', 'continent'])['total_renewable_consumption'].sum().unstack()
    grouped_data.reset_index(level=0, inplace=True)

    # Adjusts the plot
    grouped_data.plot(x='year', ylabel='Terrawatt Hour', kind='bar', stacked=True,figsize=(20,6),
            title='Global Renewable Consumption 1990 - 2024')
    plt.savefig('.\plots\Global_Renewable_Consumption_1990_2024.png')
    plt.show()
    plt.close()

# Calls the function to plot the stacked bar chart  
plot_renewable_energy_consumption_continental(df)

def plot_renewable_energy_consumption_per_capita(df: pd.DataFrame) -> None:
    """
    Plots a stacked bar chart with the total renewable energy consumption per capita by continent over the years.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame with the data of the continents.
    """
    # Groups the data by year and continent
    grouped_data = df.groupby(['year', 'continent'])['renewable_consumption_per_capita'].sum().unstack()
    grouped_data.reset_index(level=0, inplace=True)

    # Adjusts the plot
    grouped_data.plot(x='year', ylabel='Terrawatt Hour', kind='bar', stacked=True,figsize=(20,6),
            title='Global Renewable Consumption per Capita 1990 - 2024')
    plt.savefig('.\plots\Global_Renewable_Consumption_per_Capita_1990_2024.png')
    plt.show()
    plt.close()

# Calls the function to plot the stacked bar chart
plot_renewable_energy_consumption_per_capita(df)