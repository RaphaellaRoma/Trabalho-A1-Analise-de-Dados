# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:52:47 2024

@author: raphy
"""
import numpy as np
import pandas as pd

df = pd.read_csv("..\data\World Energy Consumption.csv")
print(df.info())
print(df.head())

columns = df.columns

def renewable_energy_production_frame(df):
    # country, year, bio_fuel, hydro, renewables, other_renewables, solar, wind, electricity_demand, electricity_demand_per_capita, electricity_generation
    pass
def renewable_energy_consumption_frame(df):
    #country, year, bio_fuel, hydro, renewables, other_renewables, solar, wind
    pass

def GDP_and_fossil_energy_consumption(df):
    # coal, fossil gas, oil, GDP, country
    pass