import pandas as pd
import plotly.express as px

df = pd.read_csv('.\data\World Energy Consumption.csv')
# Como a distribuição de fontes renováveis de energia varia por continente ao longo dos anos?

# pd.set_option('display.max_rows', None)    
# print(df["country"].value_counts().sort_index())

countries_by_continent_map = {
    "Antarctica": ["Antarctica"],
    "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", "Congo", "Cote d'Ivoire", "Democratic Republic of Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
    "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"],
    "Europe": ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom"],
    "América do Norte": ["Canada", "Greenland", "Mexico", "United States"],
    "América Central e Caribe": ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago"],
    "América do Sul": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
    "Oceania": ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
}

def continent_identifier(country):
    for continent, countries in countries_by_continent_map.items():
        if country in countries:
            return continent
    return None
        
def renewable_energy_consumption_by_continent(df):
    df["continent"] = df["country"].apply(continent_identifier)
    df_continents = df[["continent", "year", "biofuel_consumption", "hydro_consumption", "low_carbon_consumption", "nuclear_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"]]
    no_nulls_rows = df_continents.dropna(subset=["biofuel_consumption", "hydro_consumption", "low_carbon_consumption", "nuclear_consumption", "other_renewable_consumption", "renewables_consumption", "solar_consumption", "wind_consumption"], how='any') 
    new_df = no_nulls_rows[(no_nulls_rows['year'] >= 1990) & (no_nulls_rows['year'] <= 2024)]
    return new_df

renewable_energy_consumption_continental = renewable_energy_consumption_by_continent(df)

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

grouped_data = renewable_energy_consumption_continental.groupby(['year', 'continent'])['total_renewable_consumption'].sum().reset_index()

fig = px.bar(grouped_data, x='continent', y='total_renewable_consumption', color='continent', animation_frame='year', animation_group='continent', range_y=[0, 35000], title='Renewable Energy Consumption by Continent')
fig.show()