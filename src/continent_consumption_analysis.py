"""Stacked Column Chart Generation Module

This module contains the graph generating function
on the consumption of renewable energy on the continents over the years.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Access to raw data
df = pd.read_csv('.\data\World Energy Consumption.csv')

# Creates a dictionary that associates countries with their continents 
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
    df_continents = df[["continent", "year", "biofuel_consumption", "hydro_consumption", "low_carbon_consumption", "nuclear_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"]]
    # Filters the lines without empty values
    no_nulls_rows = df_continents.dropna(subset=["biofuel_consumption", "hydro_consumption", "low_carbon_consumption", "nuclear_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"], how='any')
    # Filters the valid lines with years between 1990 and 2024
    new_df = no_nulls_rows[(no_nulls_rows['year'] >= 1990) & (no_nulls_rows['year'] <= 2024)]
    return new_df

# Calls the function to create the new DataFrame
renewable_energy_consumption_continental = renewable_energy_consumption_by_continent(df)

# Creates a new colum in the new DF with the sum of the different types of renewable energy
renewable_energy_consumption_continental['total_renewable_consumption'] = (
    renewable_energy_consumption_continental['biofuel_consumption'] +
    renewable_energy_consumption_continental['hydro_consumption'] +
    renewable_energy_consumption_continental['low_carbon_consumption'] +
    renewable_energy_consumption_continental['nuclear_consumption'] +
    renewable_energy_consumption_continental['other_renewable_consumption'] +
    renewable_energy_consumption_continental['renewables_consumption'] +
    renewable_energy_consumption_continental['solar_consumption'] +
    renewable_energy_consumption_continental['wind_consumption']
)

# Plots the stacked bar chart
def plot_renewable_energy_consumption_continental(renewable_energy_consumption_continental: pd.DataFrame) -> None:
    """
    Plots a stacked bar chart with the total renewable energy consumption by continent over the years.

    Parameters
    ----------
    renewable_energy_consumption_continental : pd.DataFrame
        The DataFrame with the data of the continents.
    """
    # Groups the data by year and continent
    grouped_data = renewable_energy_consumption_continental.groupby(['year', 'continent'])['total_renewable_consumption'].sum().unstack()
    grouped_data.reset_index(level=0, inplace=True)

    # Adjusts the plot
    grouped_data.plot(x='year', ylabel='Terrawatt Hour', kind='bar', stacked=True,figsize=(20,6),
            title='Global Renewable Consumption 1990 - 2024')
    plt.savefig('.\plots\Global_Renewable_Consumption_1990_2024.png')
    plt.show()
    plt.close()

# Calls the function to plot the stacked bar chart  
plot_renewable_energy_consumption_continental(renewable_energy_consumption_continental)